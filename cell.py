from window import Window
from point import Point
from line import Line


class Cell:

    def __init__(self, window=None):
        self.__window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.visited = False

    
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        top_line    = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        left_line   = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        right_line  = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        bottom_line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))

        if self.__window:
            self.__window.draw_line(top_line,    "black" if self.has_top_wall    else "white")
            self.__window.draw_line(left_line,   "black" if self.has_left_wall   else "white")
            self.__window.draw_line(right_line,  "black" if self.has_right_wall  else "white")
            self.__window.draw_line(bottom_line, "black" if self.has_bottom_wall else "white")


    def draw_move(self, to_cell, undo=False):
        color = "grey" if undo else "red"
        c1 = Point(self.__x1/2+self.__x2/2, self.__y1/2+self.__y2/2)
        c2 = Point(to_cell.__x1/2+to_cell.__x2/2, to_cell.__y1/2+to_cell.__y2/2)
        l = Line(c1, c2)

        if self.__window:
            self.__window.draw_line(l, color)