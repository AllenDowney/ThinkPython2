"""Exploration of Vectors and Frames.

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from __future__ import print_function, division

import sys
import numpy
import math

def println(s):
    print(s, '\n')

class FrameError(ValueError):
    """Represents a problem with frame of reference."""

class Vector:
    def __init__(self, array, frame=None):
        """A vector is an array of coordinates and a frame of reference.

        array: 
        frame: Frame object
        """
        self.array = array
        self.frame = frame

    def __str__(self):
        if self.frame == None:
            return '^{O}%s' % (str(self.array), )
        else:
            return '^{%s}%s' % (str(self.frame), str(self.array))

    def __add__(self, other):
        if self.frame != other.frame:
            raise FrameError("Vectors must be relative to the same frame.")

        return Vector(self.array + other.array, self.frame)

    @staticmethod
    def from_list(t, frame=None):
        """Makes a vector from a list.

        t: list of coordinates
        frame: reference Frame
        """
        return Vector(numpy.array(t), frame)


class Rotation:
    def __init__(self, array):
        self.array = array
    
    def __str__(self):
        return 'Rotation\n%s' % str(self.array)

    def __neg__(self):
        return Rotation(-self.array)

    def __mul__(self, other):
        """Apply the rotation to a Vector."""
        return numpy.dot(self.array, other.array)

    __call__ = __mul__

    @staticmethod
    def from_axis(axis, theta):
        x, y, z = numpy.ravel(axis.array)
        c = math.cos(theta)
        u = 1.0-c
        s = math.sqrt(1.0-c*c)
        xu, yu, zu = x*u, y*u, z*u
        v1 = [x*xu + c, x*yu - z*s, x*zu + y*s]
        v2 = [x*yu + z*s, y*yu + c, y*zu - x*s]
        v3 = [x*zu - y*s, y*zu + x*s, z*zu + c]
        return Rotation(numpy.array([v1, v2, v3]))

    def to_axis(self):
        # return the equivalent angle-axis as (khat, theta)
        pass

    def transpose(self):
        return Rotation(numpy.transpose(self.array))

    inverse = transpose
    

class Transform:
    """Represents a transform from one Frame to another."""

    def __init__(self, rot, org, source=None):
        """Instantiates a Transform.

        rot: Rotation object
        org: origin Vector
        source: source Frame
        """
        self.rot = rot
        self.org = org
        self.dest = org.frame
        self.source = source
        self.source.add_transform(self)

    def __str__(self):
        """Returns a string representation of the Transform."""
        if self.dest == None:
            return '%s' % self.source.name
            return '_{%s}^{O}T' % self.source.name
        else:
            return '_{%s}^{%s}T' % (self.source.name, self.dest.name)
            
    def __mul__(self, other):
        """Applies a Transform to a Vector or Transform."""
        if isinstance(other, Vector):
            return self.mul_vector(other)

        if isinstance(other, Transform):
            return self.mul_transform(other)

    __call__ = __mul__

    def mul_vector(self, p):
        """Applies a Transform to a Vector.

        p: Vector

        Returns: Vector
        """
        if p.frame != self.source:
            raise FrameError(
                "The frame of the vector must be the source of the transform")
        return Vector(self.rot * p, self.dest) + self.org

    def mul_transform(self, other):
        """Applies a Transform to another Transform.

        other: Transform

        Returns Transform
        """
        if other.dest != self.source:
            raise FrameError(
                "This frames source must be the other frame's destination.")

        rot = Rotation(self.rot * other.rot)
        t = Transform(rot, self * other.org, other.source)
        return t

    def inverse(self):
        """Computes the inverse transform.

        Returns: Transform
        """
        irot = self.rot.inverse()
        iorg = Vector(-(irot * self.org), self.source)
        t = Transform(irot, iorg, self.dest)
        return t


class Frame:
    """Represents a frame of reference."""

    # list of Frames
    roster = []
    
    def __init__(self, name):
        """Instantiate a Frame.

        name: string
        """
        self.name = name
        self.transforms = {}
        Frame.roster.append(self)

    def __str__(self): 
        return self.name

    def add_transform(self, transform):
        """A frames is defined by a Transform relative to another Frame.

        transform: Transform object
        """
        if transform.source != self:
            raise FrameError("Source of the transform must be this Frame.")

        if transform.dest:
            self.transforms[transform.dest] = transform

    def dests(self):
        """Returns a list of the Frames we know how to Transform to."""
        return self.transforms.keys()
    

class Vertex:
    """Represents a node in a graph."""

    def __init__(self, frame):
        self.frame = frame
        self.dist = 1000000
        self.out = []

    def __str__(self):
        return '%s %d' % (self.frame.name, self.dist)


def shortest_path(start, frames):
    """For a given list of frames and a starting frame,
    find the shortest path of transforms from the
    starting frame to all other frames.
    The 'distance' is the number of inverse transformations
    that must be calculated.
    The result is a dictionary of vertices, where
    each vertex is labeled with the frame it corresponds
    to, the distance from the starting frame, and the prev
    frame along the path from start. """

    map = dict([(f, Vertex(f)) for f in frames])
    
    length = {}
    for v in map.values():
        for dest in v.frame.transforms:
            w = map[dest]
            v.out.append(w)
            length[(v, w)] = 0

            w.out.append(v)
            length[(w, v)] = 1

    s = map[start]
    s.dist = 0
    queue = [s]

    while queue:
        v = queue.pop()
        for w in v.out:
            d = v.dist + length[(v,w)]
            if d < w.dist:
                w.dist = d
                w.prev = v
                if w not in queue: queue.append(w)

    return map

def print_shortest_path(map):
    for source, v in map.items():
        try:
            v.prev
            print(source, v.dist, v.prev.frame)
        except:
            print(source, v.dist)

def print_length(length):
    for v, w in length:
        print(v.frame.name, w.frame.name, length[(v, w)])
    print()


def main(name):

    theta = math.pi/2

    #v_o = Vector.from_list([0, 0, 0], None)
    origin = Frame('O')
    #o_trans = Transform(None, v_o, origin)

    xhat = Vector.from_list([1, 0, 0], origin)
    rx = Rotation.from_axis(xhat, theta)
    a = Frame('A')
    t_ao = Transform(rx, xhat, a)

    yhat = Vector.from_list([0, 1, 0], a)
    ry = Rotation.from_axis(yhat, theta)
    b = Frame('B')
    t_ba = Transform(ry, yhat, b) 
    
    zhat = Vector.from_list([0, 0, 1], b)
    rz = Rotation.from_axis(zhat, theta)
    c = Frame('C') 
    t_cb = Transform(rz, zhat, c)

    p_c = Vector.from_list([1, 1, 1], c)
    println(p_c)

    p_b = t_cb(p_c)
    println(p_b)

    p_a = t_ba(p_b)
    println(p_a)

    p = t_ao(p_a)
    println(p)

    map = shortest_path(origin, Frame.roster)
    print_shortest_path(map)
    
    cbao = t_ao(t_ba(t_cb))
    p = cbao(p_c)
    println(p)

    inv = cbao.inverse()
    p_c = inv(p)
    println(p_c)

    map = shortest_path(origin, Frame.roster)
    print_shortest_path(map)

        
if __name__ == '__main__':
    main(*sys.argv)
