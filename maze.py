from graphics import Window, Line, Point
from cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed

        if self._seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell._visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j]._visited:
                to_visit.append((i-1, j))
            if i+1 < self._num_cols and not self._cells[i+1][j]._visited:
                to_visit.append((i+1, j))
            if j > 0 and not self._cells[i][j-1]._visited:
                to_visit.append((i, j-1))
            if j+1 < self._num_rows and not self._cells[i][j+1]._visited:
                to_visit.append((i, j+1))
            if to_visit == []:
                self._draw_cell(i, j)
                return
            else:
                next_cord = random.randint(0, len(to_visit)-1)
                next_cell = self._cells[to_visit[next_cord][0]][to_visit[next_cord][1]]
                if  i+1 == to_visit[next_cord][0]:
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                if i-1 == to_visit[next_cord][0]:
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                if j+1 == to_visit[next_cord][1]:
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                if j-1 == to_visit[next_cord][1]:
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                self._break_walls_r(to_visit[next_cord][0], to_visit[next_cord][1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j]._visited = False

    def solve(self):
        return self._solve_r(i=0, j=0)
    
    def _solve_r(self, i, j):
        self._animate()
        goal = self._cells[self._num_cols - 1][self._num_rows - 1]
        current_cell = self._cells[i][j]
        current_cell._visited = True
       
        if current_cell == goal:
            return True
        #left move
        if i > 0 and not self._cells[i-1][j]._visited and not current_cell.has_left_wall:
            current_cell.draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i-1][j], undo=True)     
        #right move
        if i+1 < self._num_cols and not self._cells[i+1][j]._visited and not current_cell.has_right_wall:
            current_cell.draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i+1][j], undo=True)
        # up move
        if j > 0 and not self._cells[i][j-1]._visited and not current_cell.has_top_wall:
            current_cell.draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j-1], undo=True)
        # down move
        if j+1 < self._num_rows and not self._cells[i][j+1]._visited and not current_cell.has_bottom_wall:
            current_cell.draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j+1], undo=True)
        return False





            
        





            
            

            





        







