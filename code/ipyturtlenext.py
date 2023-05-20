# The MIT License (MIT)
#
# Copyright (c) 2021 Hebi@ninja-python.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import annotations
import math
import time
from ipycanvas import MultiCanvas

SLOW_DOWN = 0.05

class Turtle(MultiCanvas):
    def __init__(self, width=320, height=320):
        super().__init__(2, width=width, height=height)

        self._turtle_on:bool = True
        self._pen_on:bool = True
        self._show_frame:bool = True
        self._slow_down:bool = True

        self._turtle_location_x = 0.0
        self._turtle_location_y = 0.0
        self._turtle_heading = 0.0

        self._turtle_heading_x = 1.0
        self._turtle_heading_y = 0.0
        self._turtle_height = 20
        self._turtle_width = 10

        self._current_color = "Green"
        self._current_color_rgb = None

        self._canvas = self[0]
        self._turtle_canvas = self[1]

        self._reset()
        self._draw()
        # self._turtle_canvas.flush()
    
    def _reset(self):
        self._turtle_on = True
        self._pen_on = True
        self._turtle_location_x = 0
        self._turtle_location_y = 0
        self._turtle_heading = 90.0
        self._turtle_heading_x = 1.0
        self._turtle_heading_y = 0.0
        self._clear_canvas(self._turtle_canvas)
        self._clear_canvas(self._canvas)
        if self._show_frame:
            self._canvas.stroke_rect(0, 0, self.width, self.height)

    def _draw(self, start=None, end=None, color=None):

        if self._slow_down:
            time.sleep(SLOW_DOWN)

        if start and end and color:
            self._canvas.set_transform(1,0,0,-1,self.width/2,self.height/2)
            self._canvas.begin_path()
            self._canvas.move_to(start[0],start[1])
            self._canvas.line_to(end[0],end[1])
            self._canvas.stroke_style=color
            self._canvas.close_path()
            self._canvas.stroke()

        self._clear_canvas(self._turtle_canvas)
        
        if self._turtle_on:
            self._draw_turtle()

    def _clear_canvas(self, canvas):
        canvas.reset_transform()
        canvas.clear()

    def _draw_turtle(self):
        
        hX = 0.5 * self._turtle_height * self._turtle_heading_x
        hY = 0.5 * self._turtle_height * self._turtle_heading_y

        noseX = self._turtle_location_x + hX
        noseY = self._turtle_location_y + hY

        leftLegX = self._turtle_location_x - 0.5 * self._turtle_width * self._turtle_heading_y - hX
        leftLegY = self._turtle_location_y + 0.5 * self._turtle_width * self._turtle_heading_x - hY

        rightLegX = self._turtle_location_x + 0.5 * self._turtle_width * self._turtle_heading_y - hX
        rightLegY = self._turtle_location_y - 0.5 * self._turtle_width * self._turtle_heading_x - hY
        
        self._turtle_canvas.set_transform(1,0,0,-1,self.width/2,self.height/2)
     
        self._turtle_canvas.begin_path()
        self._turtle_canvas.move_to(noseX,noseY)
        self._turtle_canvas.line_to(rightLegX,rightLegY)
        self._turtle_canvas.line_to(leftLegX,leftLegY)
        self._turtle_canvas.close_path()
        self._turtle_canvas.stroke()

    def position(self):
        return self._turtle_location_x, self._turtle_location_y

    def forward(self, length):
        precision = 4
        start = (round(self._turtle_location_x,precision),
                 round(self._turtle_location_y,precision))
        self._turtle_location_x += length * self._turtle_heading_x
        self._turtle_location_y += length * self._turtle_heading_y
        end = (round(self._turtle_location_x, precision),
               round(self._turtle_location_y, precision))

        if self._pen_on:
            color = self._current_color
            if len(self._current_color)==0:
                color = "rgb({},{},{})".format(self._current_color_rgb[0],
                                               self._current_color_rgb[1],
                                               self._current_color_rgb[2])
            self._draw(start,end,color)
        else:
            self._draw()


    def back(self, length):
        self.forward(-length)

    def heading(self):
        return self._turtle_heading

    def goto(self, x, y=None):
        if y is None:
            y = x[1]
            x = x[0]
        self._turtle_location_x = float(x)
        self._turtle_location_y = float(y)
        self._draw()

    def setpos(self, x, y=None):
        return self.goto(x, y)

    def setposition(self, x, y=None):
        return self.goto(x, y)

    def left(self, degree=None):
        if degree is None:
            degree = 90
        self._turtle_heading += degree
        self._turtle_heading = self._turtle_heading % 360

        hx = math.cos(math.radians(self._turtle_heading))
        hy = math.sin(math.radians(self._turtle_heading))

        self._turtle_heading_x = hx
        self._turtle_heading_y = hy
        self._draw()

    def right(self, degree=None):
        if degree is None:
            degree = 90
        self.left(-degree)

    def penup(self):
        self._pen_on = False

    def pendown(self):
        self._pen_on = True

    def slowdown(self, value:bool=True)->None:
        self._slow_down = value
    
    def showframe(self,value:bool=True)->None:
        self._show_frame = value

    def isdown(self):
        return self._pen_on

    def hideturtle(self):
        self._turtle_on = False
        self._draw()

    def showturtle(self):
        self._turtle_on = True
        self._draw()

    def isvisible(self):
        return self._turtle_on

    def reset(self):
        self._reset()
        self.pencolor(0, 0, 0)
        self.forward(0)

    def pencolor(self,r=-1,g=-1,b=-1):
        if r == -1:
            if len(self._current_color)==0:
                return  self._current_color_rgb
            else:
                return self._current_color
        elif type(r) == str:
            self._current_color = r
            self._current_color_rgb = None
        else:
            self._current_color = ""
            self._current_color_rgb = (r,g,b)
        self.forward(0)
