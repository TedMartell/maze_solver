from graphics import Window, Line, Point 


def main():
    win = Window(800, 600)  # Adjust the size as needed
    start_point = Point(100,100)
    end_point = Point(200,200)
    lines = Line(start_point, end_point)
    win.draw_line(lines, fill_colour="red")
    win.wait_for_close()

if __name__ == "__main__":
    main()

