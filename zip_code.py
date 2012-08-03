"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

"""This is the simplest solution to the problem; I made no effort
to parse the HTML code.  Instead I just search for some key words.

An alternative would be to use the HTMLParser module:
http://docs.python.org/library/htmlparser.html

"""

import urllib

zipcode = '02492'

url = 'http://uszip.com/zip/' + zipcode
conn = urllib.urlopen(url)

for line in conn.fp:
    line = line.strip()
    if 'Population' in line:
        print line
    if 'Longitude' in line: 
        print line
    if 'Latitude' in line: 
        print line

conn.close()
