"""Example using the remote_object wrapper for Pyro.

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import sys
import remote_object

def main(script, name='bob', *args):
    ns = remote_object.NameServer()
    server = ns.get_proxy(name)

    print server.mul(111,9)
    print server.add(100,222)
    print server.sub(222,100)
    print server.div(2.0,9.0)
    print server.mul('*',10)
    print server.add('String1','String2')

if __name__ == '__main__':
    main(*sys.argv)
