"""Wrapper for Pyro: Python Remote Objects.

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import sys
import threading
import socket
import os
import signal

import Pyro.core
import Pyro.util
import Pyro.naming
import Pyro.errors

DEFAULT_NS_HOST = 'acl.olin.edu'


class MyThread(threading.Thread):
    """MyThread is a wrapper for threading.Thread that improves
    the syntax for creating and starting threads."""
    def __init__(self, target, *args):
        threading.Thread.__init__(self, target=target, args=args)
        self.start()


class Watcher:
    """The Watcher class solves two problems with multithreaded
    programs in Python, (1) a signal might be delivered
    to any thread (which is just a malfeature) and (2) if
    the thread that gets the signal is waiting, the signal
    is ignored (which is a bug).

    The watcher is a concurrent process (not thread) that
    waits for a signal and then kills the process that contains the
    active threads.  See Appendix A of The Little Book of Semaphores.

    I have only tested this on Linux.  I would expect it to
    work on OS X and not work on Windows."""
    
    def __init__(self, callback=None):
        """ Creates a child thread, which returns.  The parent
        thread waits for a KeyboardInterrupt and then kills
        the child thread.
        """
        self.child = os.fork()
        if self.child == 0:
            return
        else:
	    self.watch(callback)

    def watch(self, callback=None):
        """Waits for a KeyboardInterrupt and then kills the child process."""
        try:
            os.wait()
        except KeyboardInterrupt:
            # I put the capital B in KeyBoardInterrupt so I can
            # tell when the Watcher gets the SIGINT
            if callback:
                callback()
            print 'KeyBoardInterrupt'
            self.kill()
        sys.exit()

    def kill(self):
        """Kills the child process."""
        try:
            os.kill(self.child, signal.SIGKILL)
        except OSError:
            pass


def get_ip_addr():
    """Get the real IP address of this machine."""
    csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csock.connect(('www.google.com', 80))
    (addr, port) = csock.getsockname()
    csock.close()
    return addr


class NameServer:
    """A NameServer object is a proxy for the name server running
    on a remote host."""

    def __init__(self, ns_host=DEFAULT_NS_HOST):
        """Locates the name server on the given host."""
        self.ns_host = ns_host
        locator = Pyro.naming.NameServerLocator()
        self.ns = locator.getNS(host=ns_host, port=9090)

    def get_proxy(self, name):
        """Looks up a remote object by name and creates a proxy for it."""
        try:
            uri = self.ns.resolve(name)
        except Pyro.errors.NamingError:
            type, value, traceback = sys.exc_info()
            print 'Pyro NamingError:', value
            sys.exit(1)

        return Pyro.core.getProxyForURI(uri)

    def query(self, name, group=None):
        """Checks whether the given name is registered in the given group.

        Returns 1 if the name is a remote object, 0 if it is a group,
        and -1 if it doesn't exist."""
        t = self.ns.list(group)
        for k, v in t:
            if k == name:
                return v
        return -1

    def create_group(self, name):
        """Creates a group with the given name."""
        self.ns.createGroup(name)
    
    def delete_group(self, name):
        """Deletes a group with the given name."""
        self.ns.deleteGroup(name)
    
    def get_remote_object_list(self, prefix='', group=None):
        """Returns a list of the remote objects in the given group
        that start with the given prefix."""
        t = self.ns.list(group)
        u = [s for (s, n) in t if n==1 and s.startswith(prefix)]
        return u

    def clear(self, prefix='', group=None):
        """Unregister all objects in the given group that start
        with the given prefix."""
        t = self.ns.list(group)

        for (s, n) in t:
            if not s.startswith(prefix): continue
            if n==1:
                if group:
                    s = '%s.%s' % (group, s)
                print 'Unregistering', s
	        self.ns.unregister(s)
    

class RemoteObject(Pyro.core.ObjBase):
    """Extends Pyro.core.ObjBase and provides a higher level of abstraction.

    Objects that want to be available remotely should inherit
    from this class, and either (1) don't override __init__ or
    (2) call RemoteObject.__init__ explicitly"""

    def __init__(self, name=None, ns=None):
        """Creates a new RemoteObject with the given name and
        registers with the given name server.  If name is omitted,
        one is generated based on the object id.  If ns is omitted,
        it uses the default name server.
        """
        Pyro.core.ObjBase.__init__(self)

        if name == None:
            name = 'remote_object' + str(id(self))
        self.name=name
        
        if ns == None:
            ns = NameServer()

        self.connect(ns, name)
        
    def connect(self, ns, name):
        """Connects to the given name server with the given name."""

        # create the daemon
        addr = get_ip_addr()
        self.pyro_daemon = Pyro.core.Daemon(host=addr)
        self.pyro_daemon.useNameServer(ns.ns)

        # instantiate the object and advertise it
        try:
            print 'Connecting remote object', name
            self.uri = self.pyro_daemon.connect(self, name)
        except Pyro.errors.NamingError:
            print 'Pyro NamingError: name already exists or is illegal'
            sys.exit(1)

        return self.name

    def requestLoop(self):
        """Runs the request loop until an exception occurs."""
        try:
            self.pyro_daemon.requestLoop()
        except:
            self.cleanup()
            if sys.exc_type != KeyboardInterrupt:
                raise sys.exc_type, sys.exc_value

    def cleanup(self):
        """Removes this object from the name server."""
        print 'Shutting down remote object', self.name
        try:
            self.pyro_daemon.disconnect(self)
        except:
            print "Did not disconnect cleanly."
            raise sys.exc_type, sys.exc_value
        self.stopLoop()
        self.pyro_daemon.shutdown()

    def threadLoop(self):
        """Runs the request loop in a separate thread."""
        self.thread = threading.Thread(target=self.stoppableLoop)
        self.thread.start()
        
    def stoppableLoop(self):
        """Run handleRequests until another thread clears self.running."""
        self.running = True
        try:
            while self.running:
                self.pyro_daemon.handleRequests(0.1)
        finally:
            self.cleanup()

    def stopLoop(self):
        """If stoppableLoop is running, stops it."""
        self.running = False

    def join(self):
        """Waits for the threadLoop to complete."""
        if hasattr(self, 'thread'):
            self.thread.join()


def main(script, action='', prefix='unlikely_prefix', group=None):

    if action == '':
        print 'To list all remote objects on the name server, run'
        print 'python remote_object.py list'
        print
        print 'To remove objects from the name server, run'
        print 'python remote_object.py clean PREFIX'
        print
        print 'where you replace PREFIX with the name of a remote'
        print 'object, or the common prefix of several objects.'

    if action == 'clear':
        ns = NameServer()
        if prefix == '':
            prefix = 'remote_object'
        ns.clear(prefix, group)

    if action == 'list':
        ns = NameServer()
        t = ns.get_remote_object_list(prefix, group)
        print t


if __name__ == '__main__':
    main(*sys.argv)
