"""This program is part of an exercise in
Think Python: An Introduction to Software Design, by Allen Downey.

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

This module uses color_list and Visual Python to 
draw the X11 colors as spheres in 3-D RGB space.

The size of the spheres (can be) proportional to the distance
to the nearest neighbor.

Users can zoom and rotate using the usual Visual interface:

* Drag middle button up and down to zoom in and out.

* Drag right button to rotate.

Clicking on a sphere prints the color names and toggles a label.

Usage:

python color_space.py

or

python color_space.py resize

"""

import sys
from visual import *

def draw_spheres(rgbs, radius=10):
    """rgbs is a dictionary that maps from an rgb tuple to a
    list of color names.  rgb values are in the range 0-255.

    draws one sphere for each rgb tuple with the given radius,
    and returns a list of sphere objects.

    the sphere objects have the color names as an attribute.
    """
    spheres = []
    for rgb, names in rgbs:
        pos = vector(rgb)
        color = pos/255.0
        obj = sphere(pos=pos, radius=radius, color=color)
        obj.names = names
        spheres.append(obj)
    return spheres

def find_nearest_neighbor(s, spheres):
    """of the objects in (spheres) find the one closest to s
    and return a tuple (distance, closest_object)
    """
    t = [(mag(s.pos - s2.pos), s2) for s2 in spheres if s2 is not s]
    return min(t)

def set_size(spheres, factor=0.7):
    """for each sphere, find d, the distance to the nearest neighbor
    and set radius = factor * d
    """
    for s in spheres:
        d, n = find_nearest_neighbor(s, spheres)
        s.radius = factor * d

def find_biggest_hole(spheres):
    """of the web safe colors, find the one whose nearest neighbor
    is the farthest.  the answer is (51, 51, 255) or #3333ff
    which is a nive shade of blue that deserves a name.
    """
    s = sphere(color=(1,1,1))
    t = range(0, 256, 51)

    res = []
    for r in t:
        for g in t:
            for b in t:
                pos = (r,g,b)
                s.pos = pos
                d, n = find_nearest_neighbor(s, spheres)
                print d, pos
                res.append((d, pos))

    d, pos = max(res)
    print 'winner', d, pos
    s.pos = pos
    s.radius = d
    s.color = vector(pos)/255.0

def find_closest_sphere(m, spheres):
    """given the mouse information in (m), find the closest
    sphere that is intersected by the line from the camera
    to the mouse click.
    """
    c = m.camera
    r = m.ray

    t = []
    for obj in spheres:
        d = obj.pos-c          # vector from camera to object
        dist = dot(d, r)       # distance from the camera
        proj = dist * r        # projection of d onto ray
        off = mag(d - proj)    # perp dist of object from ray line

        # make a list of objects in front of us that intersect the line
        if dist > 0 and off < obj.radius:
            t.append((dist, obj))

    # find the intersected object closest to the camera
    if t:
        dist, obj = min(t)
        return obj
    else:
        return None

def toggle_label(obj):
    """add or remove the label from a color sphere
    """
    try:
        obj.label.visible ^= 1
    except:
        obj.label = label(pos=obj.pos, text=obj.names[0], 
                          xoffset=8, yoffset=8, 
                          space=obj.radius/2, height=10, border=6)

def main(script, *args):
    """create the display and wait for user events
    """

    # set up the scene
    scene.title = "X11 color space"
    scene.height = 500
    scene.width = 500
    scene.range = (256, 256, 256)
    scene.center = (128, 128, 128)

    # read the colors
    from color_list import read_colors
    colors, rgbs = read_colors()

    # add an entry for the biggest unnamed color in X11 space
    name = 'allen blue'
    rgbs.append(((51,51,255), [name]))

    # draw the spheres
    spheres = draw_spheres(rgbs)
    if 'resize' in args:
        set_size(spheres)

    #find_biggest_hole(spheres)

    print """
    Left-click on a sphere to see the color name(s).

    Drag the middle mouse up/down to zoom in/out.

    Drag the right mouse to rotate.
    """

    # wait for mouse clicks
    while 1:
         if scene.mouse.clicked:
             m = scene.mouse.getclick()
             obj = find_closest_sphere(m, spheres)
             if obj:
                 print ', '.join(obj.names)
                 toggle_label(obj)

if __name__ == '__main__':
    main(*sys.argv)
