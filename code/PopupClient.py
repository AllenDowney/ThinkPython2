"""This module is part of an exercise for
Think Python: an Introduction to Software Design

Copyright 2011 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import sys
import Pyro.errors

from remote_object import NameServer


def main(script, to='downey', message='hello', sender='downey', *args):
    """Contact the remote object with the given name and
    invoke popup with the given message"""
    ns = NameServer()
    try:
        name = 'popup_%s' % to
        server = ns.get_proxy(name)
    except Pyro.errors.NamingError:
        print "I can't find a remote object named " + name
        return
    print server.popup(message, sender)


if __name__ == '__main__':
    main(*sys.argv)
