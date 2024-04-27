from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Window")
        c = Canvas(self.__root, width=width, height=height)
        c.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)   
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

        



    

        

