import commun.table

import tkinter as tk


class rootWindow():
    def __init__(self):
        self.__cellSize = 60

        self.tkInit()

        self.__table = commun.table.Table()

        self.main()
        self.__root.mainloop()

    def tkInit(self):
        self.__root = tk.Tk()
        self.__width = self.__root.winfo_screenwidth()
        self.__height = self.__root.winfo_screenheight()
        self.__root.config(width=self.__width, height=self.__height)

        self.__frame = tk.Frame(self.__root, background='black')
        self.__frame.config(width=self.__width, height=self.__height)
        self.__frame.grid(row=0, column=0)
        self.__canvas = tk.Canvas(self.__frame)
        self.__canvas.config(width=(self.__cellSize*16), height=(self.__cellSize*13),
                             highlightthickness=0, bd=0, bg="white")

    def main(self):
        self.displayHex()
        self.updateDisplay()

    def updateDisplay(self):
        self.__canvas.pack()

    def displayHex(self):

        # Gets Grid
        grid = self.__table.getGrid()

        # Gets relative values for points generation
        xSpace = self.__cellSize
        ySpace = xSpace/2
        xCellSpace = xSpace
        yCellSpace = xSpace*1.50

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col].getState() != 0:
                    x = (xCellSpace*col)+(xSpace)
                    y = (yCellSpace*row)+(ySpace*3)

                    points = [(x, y),
                              (x+xSpace, y-ySpace),
                              (x+(xSpace*2), y),
                              (x+(xSpace*2), y+(2*ySpace)),
                              (x+xSpace, y+(3*ySpace)),
                              (x, y+(2*ySpace))]

                    self.__canvas.create_polygon(
                        points, fill="red", outline="black", width=3)


def run():
    win = rootWindow()


run()
