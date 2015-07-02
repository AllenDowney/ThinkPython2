This document describes some of the changes I am planning for the second edition of Think Python, which I am posting here for public comment.

1) Update for compliance with Python 2/3.  I will revise all code and examples to work with both Python 2 and 3.  In chapter 1 I will discuss the status of 2/3 and present ``from __future__ import print_function``.  Then I will use print function syntax throughout.  There are only a few other differences between 2 and 3 that come up, and they are already discussed in the first edition.

2) In the first chapter I will provide instructions for getting started with Python in a browser, so beginners can get started without dealing with installation problems.

3) In a later chapter I will provide instructions for transitioning to a local Python IDE, probably IDLE.  Again, the goal is to minimize frustration for people who are not comfortable installing things.

4) In Chapter 4 I present a case study based on turtle graphics using Swampy, a package I wrote and maintain.  I am considering replacing Swampy with the turtle module that comes with Python, again because installing Swampy seems to be a major pain point for beginners.

5) Chapter 19 is a case study using Swampy and Tkinter.  I am considering removing this case study, for two reasons: (a) again, installing Swampy is a problem, and (b) my impression is that this chapter is not widely read or used.

6) I resisted including list comprehensions because they are not necessary and they are hard for beginners to debug.  But I am considering including them.

7) In a few places I use a dictionary instead of a set because (a) sets were not core Python at the time, and (b) I wanted to minimize the number of data structures I presented.  But I think I will include them in the next edition.

8) I have a bunch of new exercises from my classes that I can add.  At the same time I will remove some of the less interesting exercises.

9) I am considering adding a final chapter that presents the data structures in the collections class.

I will probably add to this list once I get started, but I am happy to hear comments and suggestions.  You can add line notes to this file, or send me email.
