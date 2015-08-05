"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from datetime import datetime


def main():
    print("Today's date and the day of the week:")
    today = datetime.today()
    print(today)
    print(today.strftime("%A"))

    print("Your next birthday and how far away it is:")
    #s = input('Enter your birthday in mm/dd/yyyy format: ')
    s = '5/11/1967'
    bday = datetime.strptime(s, '%m/%d/%Y')

    next_bday = bday.replace(year=today.year)
    if next_bday < today:
        next_bday = next_bday.replace(year=today.year+1)
    print(next_bday)

    until_next_bday = next_bday - today
    print(until_next_bday)

    print("Your current age:")
    last_bday = next_bday.replace(year=next_bday.year-1)
    age = last_bday.year - bday.year
    print(age)

    print("For people born on these dates:")
    bday1 = datetime(day=11, month=5, year=1967)
    bday2 = datetime(day=11, month=10, year=2003)
    print(bday1)
    print(bday2)

    print("Double Day is")
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    dd = d2 + (d2 - d1)
    print(dd)


if __name__ == '__main__':
    main()
