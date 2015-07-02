"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

from datetime import datetime

# to avoid duplicating code, I'm importing everything from Time1
from Time1 import *


def is_after(t1, t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


def increment(t1, seconds):
    """Adds seconds to a Time object."""
    assert valid_time(t1)
    seconds += time_to_int(t1)
    return int_to_time(seconds)


def mul_time(t1, factor):
    """Multiplies a Time object by a factor."""
    assert valid_time(t1)
    seconds = time_to_int(t1) * factor
    return int_to_time(seconds)


def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
    # when is my birthday this year?
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # if it has gone by, when will it be next year
    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)

    # subtraction on datetime objects returns a timedelta object
    delta = next_birthday - today
    return delta.days


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    double_day = b1 + delta
    return double_day


def datetime_exercises():
    # print today's day of the week
    today = datetime.today()
    print today.weekday()
    print today.strftime('%A')

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1967, 5, 2)
    print 'Days until birthday',
    print days_until_birthday(birthday)

    # compute the day one person is twice as old as another
    b1 = datetime(2006, 12, 26)
    b2 = datetime(2003, 10, 11)
    print 'Double Day',
    print double_day(b1, b2)


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print 'Starts at',
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print 'Run time',
    print_time(run_time)

    # what time does the movie end?
    end_time = add_times(noon_time, run_time)
    print 'Ends at',
    print_time(end_time)

    print 'Does it end after it begins?',
    print is_after(end_time, noon_time)

    print 'Home by',
    travel_time = 600      # 10 minutes
    home_time = increment(end_time, travel_time)
    print_time(home_time)

    race_time = Time()
    race_time.hour = 1
    race_time.minute = 34
    race_time.second = 05

    print 'Half marathon time',
    print_time(race_time)

    distance = 13.1       # miles
    pace = mul_time(race_time, 1/distance)

    print 'Time per mile',
    print_time(pace)

    datetime_exercises()


if __name__ == '__main__':
    main()
