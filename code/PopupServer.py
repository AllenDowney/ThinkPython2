"""This module is part of an exercise for
Think Python: an Introduction to Software Design

Copyright 2011 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import sys

from remote_object import RemoteObject
from PopupDemo import spawn_popup

class PopupServer(RemoteObject):
    """a PopupServer is a remote object that provides a method,
    popup() that takes a message and displays it in a Popup"""
    def popup(self, message, sender):
        spawn_popup(message, sender)

def main(script, name='popup_downey', *args):
    """name is the name of the remote object"""
    print 'Starting PopupServer %s...' % name
    server = PopupServer(name)
    server.requestLoop()
    
if __name__ == '__main__':
    main(*sys.argv)

