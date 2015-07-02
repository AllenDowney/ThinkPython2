"""
Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2013 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.


If you type an integer with a leading zero, you might get
a confusing error:

>>> zipcode = 02492
                  ^
SyntaxError: invalid token

Other numbers seem to work, but the results are bizarre:

>>> zipcode = 02132
>>> zipcode
1114

Can you figure out what is going on?  Hint: display the
values 01, 010, 0100 and 01000.

"""

print 01, 010, 0100, 01000


"""

The result is

1 8 64 512

which you might recognize as powers of 8.

If a number begins with 0, Python treats it as an octal number,
which means it is in base 8.

So in the example, 02132 is considered

"""

print 2 * 512 + 1 * 64 + 3 * 8 + 2

"""

which is 1114.

In Python 3, this "feature" has been removed.

"""

