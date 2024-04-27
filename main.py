from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)  # Adjust the size as needed
    x1 = 100
    x2 = 200
    y1 = 100
    y2 = 200
    cell1 = Cell(True, True, True, True, x1, x2, y1, y2, win)
    cell2 = Cell(True, True, True, True, 200, 300, 200, 300, win)

    cell1.draw()
    cell2.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()

