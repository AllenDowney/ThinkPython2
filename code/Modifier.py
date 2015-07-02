"""Example of the Observer pattern using Pyro.

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import Pyro.errors
from remote_object import NameServer


class Modifier:
    """A Modifier is an object that reads and writes the state of
    a Subject, but it is not a registered Observer."""


    def __init__(self, subject_name):
        self.subject = ns.get_proxy(subject_name)

    def modify(self):
        """Increment the state of the Subject."""
        state = self.subject.get_state()
        self.subject.set_state(state+1)
        print 'Set state ' + str(state+1)


ns = NameServer()
subject_name = 'simple_subject'
mod = Modifier(subject_name)
mod.modify()
