from graphics import Window, Line, Point
from cell import Cell
from time import sleep


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()

    def _create_cells(self):       
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
                self._draw_cell(i, j)
            self._cells.append(column)
            
      
    def _draw_cell(self, i, j):
        cell_x = self.x1 + i * self.cell_size_x
        cell_y = self.y1 + j * self.cell_size_y
        self._cells[i][j].draw(cell_x, cell_y + self.cell_size_y, cell_x + self.cell_size_x, cell_y)
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)


