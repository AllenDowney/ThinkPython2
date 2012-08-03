"""Example of the Observer pattern using Pyro.

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import random

# this import has to be here in case we get a Pyro error from an RMI
import Pyro.errors
from remote_object import RemoteObject, NameServer


class Observer(RemoteObject):
    """An Observer is an object that watches another object and reacts
    whenever the Subject changes state."""

    def __init__(self, subject_name):

        # connect to the name server
        id = random.randint(0, 1000000)
        observer_name = subject_name + '_observer%d' % id
        RemoteObject.__init__(self, observer_name)
        
        # register with the subject
        self.subject = subject_name
        ns = NameServer()
        proxy = ns.get_proxy(subject_name)
        proxy.register(observer_name)
        print "I just registered."

    # the following methods are intended to be invoked remotely

    def notify(self):
        """when the Subject is modified, it invokes notify;
        then the Observer uses get_state to see the update.
        As a simpler alternative, the Subject could pass the
        new state as a parameter."""
        print 'Notified'
        ns = NameServer()
        proxy = ns.get_proxy(self.subject)
        print 'Got proxy'
        state = proxy.get_state()
        print 'Observer notified; new state =', state

obs = Observer('simple_subject')
obs.requestLoop()

