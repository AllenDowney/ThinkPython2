"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


"""

If you run a 10 kilometer race in 43 minutes 30 seconds, what is your
average time per mile? What is your average speed in miles per hour?
(Hint: there are 1.61 kilometers in a mile).

"""

minutes = 43.5
hours = minutes / 60

km_per_mile = 1.61
km = 10
miles = km / km_per_mile 

pace = minutes / miles
mph = miles / hours

print('Pace in minutes per mile:', pace)
print('Average speed in mph:', mph)
