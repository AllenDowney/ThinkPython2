"""Example of the Observer pattern using Pyro.

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from copy import copy

# this import has to be here in case we get a Pyro error from an RMI
import Pyro.errors
from remote_object import RemoteObject, NameServer


class Subject(RemoteObject):
    """A Subject is an object that keeps track of the Observers
    watching it.  When the state of a subject changes, it
    notifies each Observer on the list."""

    def __init__(self, name):
        RemoteObject.__init__(self, name)
        self.observers = []

    def notify_observers(self):
        """notify all registered observers when the state of
        the subject changes"""
        
        for observer in copy(self.observers):
            try:
                print 'Notifying', observer
                ns = NameServer()
                proxy = ns.get_proxy(observer)
                proxy.notify()
            except Exception, x:
                # this clause should catch errors that occur
                # in the Observer code.
                print ''.join(Pyro.util.getPyroTraceback(x))
            except:
                # this clause should catch Pyro NamingErrors,
                # which occur when an observer dies.
                print 'Removing ' + observer
                self.observers.remove(observer)

    # the following methods are intended to be invoked remotely

    def register(self, name):
        """Registers a new Observer (invoked by the Observer)."""
        self.observers.append(name)
        print 'Registered ' + name


class SimpleSubject(Subject):

    def __init__(self, name, state=0):
        """The state of a SimpleSubject is a single integer named 'state'
        In a real application, the state would be a more elaborate
        data structure."""
        Subject.__init__(self, name)
        self.state = 0

    # the following methods are intended to be invoked remotely
        
    def set_state(self, state):
        """Changes the state of the Subject."""
        print 'New state', state
        self.state = state
        self.notify_observers()

    def get_state(self):
        """Gets the current state of the Subject."""
        return self.state

sub = SimpleSubject('simple_subject')
sub.requestLoop()

