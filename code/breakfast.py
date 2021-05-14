"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""



"""

If I leave my house at 6:52 am and run 1 mile at an easy pace
(8:15 per mile), then 3 miles at tempo (7:12 per mile) and
1 mile at easy pace again, what time do I get home for breakfast?

"""

easy_min = 8 + 15 / 60
tempo_min = 7 + 12 / 60

total_min = 2 * easy_min + 3 * tempo_min
print('Total minutes:', total_min)

time_hour = 6 + 52 / 60 + total_min / 60
print('Time in hours', time_hour)

hours = 7
minutes = (time_hour - hours) * 60
print('Time in hours and minutes', hours, minutes)
