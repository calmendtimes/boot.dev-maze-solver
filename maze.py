import time
import random
from cell import Cell


class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):

        self.__x1          = x1
        self.__y1          = y1
        self.__num_rows    = num_rows
        self.__num_cols    = num_cols
        self.__cell_size_x = cell_size_x 
        self.__cell_size_y = cell_size_y
        self.__window      = window
        if seed: random.seed(seed)

        self.__indent_x = (self.__window.width - self.__cell_size_x * self.__num_cols) / 2
        self.__indent_y = (self.__window.height - self.__cell_size_y * self.__num_rows) / 2  
        
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls(self.__num_rows-1, self.__num_cols-1)
        

    def __create_cells(self):
        for r in range(self.__num_rows):
            self.__cells.append([])
            for c in range(self.__num_cols):
                self.__cells[r].append(Cell(self.__window))
                self.__draw_cell(r,c)   


    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(0,0)
        self.__draw_cell(self.__num_rows-1, self.__num_cols-1)


    def __break_walls(self, r, c):
        self.__threshold = 0.2
        
        if self.__cells[r][c].visited: return
        self.__cells[r][c].visited = True

        directions = [(r,c-1,"L"), (r,c+1,"R"), (r-1,c,"U"), (r+1,c,"D")]
        can_go_to = [d for d in directions if self.__in_bounds(d[0],d[1]) and not self.__is_visited(d[0], d[1])]
        random.shuffle(can_go_to)

        for d in can_go_to:
            if not self.__is_visited(d[0], d[1]):
                self.__break_wall(*d)
                self.__break_walls(d[0], d[1])

    
    def __break_wall(self, r, c, d): # "L", "R", "U", "D"
        if d == "L": 
            self.__cells[r][c+1].has_left_wall = False
            self.__cells[r][c].has_right_wall = False
            self.__draw_cell(r, c+1)
            self.__draw_cell(r, c)
        if d == "R": 
            self.__cells[r][c-1].has_right_wall = False
            self.__cells[r][c].has_left_wall = False
            self.__draw_cell(r, c-1)
            self.__draw_cell(r, c)
        if d == "U": 
            self.__cells[r+1][c].has_top_wall = False
            self.__cells[r][c].has_bottom_wall = False
            self.__draw_cell(r+1, c)
            self.__draw_cell(r, c)
        if d == "D": 
            self.__cells[r-1][c].has_bottom_wall = False
            self.__cells[r][c].has_top_wall = False
            self.__draw_cell(r-1, c)
            self.__draw_cell(r, c)
            

    def __in_bounds(self, r,c):
        return r>=0 and r<self.__num_rows and c>=0 and c<self.__num_cols 


    def __is_visited(self, r, c):
        return self.__cells[r][c].visited

    
    def __draw_cell(self, r, c):
        x1 = c * self.__cell_size_x + self.__indent_x
        y1 = r * self.__cell_size_y + self.__indent_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        if self.__window:
            self.__cells[r][c].draw(x1,y1,x2,y2)
            self.__animate()


    def __animate(self):
        if self.__window:
            self.__window.redraw()
            time.sleep(1 / self.__num_cols / self.__num_rows)
