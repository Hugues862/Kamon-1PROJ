import commun.table

import tkinter as tk


class rootWindow():
    def __init__(self):
        # Default cell size
        self.__cellSize = 50

        # Init tkinter stuff
        self.tkInit()

        # Generate new table
        self.__table = commun.table.Table()

        # main loop
        self.main()
        self.__root.mainloop()

    def tkInit(self):
        """
        Init of tkinter elements
        """
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
        self.__canvas.bind("<Button-1>", self.printCoords)

    def main(self):
        # Main loop,

        # Display Game
        self.displayHex()

        # TK packing
        self.updateDisplay()

    def updateDisplay(self):
        self.__canvas.pack()

    def displayHex(self):
        def backgroundHex(*args):
            """Displays Background Canvas and generates points
            """
            points = [(x, y),
                      (x+xSpace, y-ySpace),
                      (x+(xSpace*2), y),
                      (x+(xSpace*2), y+(2*ySpace)),
                      (x+xSpace, y+(3*ySpace)),
                      (x, y+(2*ySpace))]
            self.__canvas.create_polygon(
                points, fill="red", outline="black", width=2)

        def mainHex():
            """Displays the hexagones on the cells ( basically displays the players )
            """

        def borders(*args):
            """Displays the borders
            """
            x, y = topLeftCoords

            def top(x, y):
                pointsBottom = [(x+(xSpace/2), y-(ySpace/2)),
                                (x+xSpace, y-ySpace)]
                for i in range(2, 7, 2):
                    pointsBottom.append((x+(xSpace*i), y))
                    pointsBottom.append((x+(xSpace*(i+1)), y-ySpace))
                pointsBottom.append((x+(xSpace*7.5), y-(ySpace/2)))

                pointsTop = []
                for i in range(len(pointsBottom)-1, -1, -1):
                    pointsTop.append(
                        (pointsBottom[i][0], (pointsBottom[i][1]-(ySpace))))

                pointsTop[0] = (pointsTop[0][0]+(xSpace/4),
                                pointsTop[0][1]+(ySpace/4))
                pointsTop[-1] = (pointsTop[-1][0]-(xSpace/4),
                                 pointsTop[-1][1]+(ySpace/4))

                points = pointsBottom+pointsTop
                self.__canvas.create_polygon(
                    points, fill="cyan", outline="black", width=3)

            def bottom(x, y):
                y = y+(ySpace*22)
                pointsBottom = [(x+(xSpace/2), y-(ySpace/2)),
                                (x+xSpace, y)]
                for i in range(2, 7, 2):
                    pointsBottom.append((x+(xSpace*i), y-ySpace))
                    pointsBottom.append((x+(xSpace*(i+1)), y))
                pointsBottom.append((x+(xSpace*7.5), y-(ySpace/2)))

                pointsTop = []
                for i in range(len(pointsBottom)-1, -1, -1):
                    pointsTop.append(
                        (pointsBottom[i][0], (pointsBottom[i][1]-(ySpace))))

                pointsBottom[0] = (pointsBottom[0][0]-(xSpace/4),
                                   pointsBottom[0][1]-(ySpace/4))
                pointsBottom[-1] = (pointsBottom[-1][0]+(xSpace/4),
                                    pointsBottom[-1][1]-(ySpace/4))

                points = pointsBottom+pointsTop
                self.__canvas.create_polygon(
                    points, fill="cyan", outline="black", width=3)

            def topLeft(x, y):
                pointsRight = [(x+(xSpace/2), y-(ySpace/2)),
                               (x, y)]
                pointsRight.append((x, y+(ySpace*2)))
                pointsRight.append((x-(xSpace*1), y+(ySpace*3)))
                pointsRight.append((x-(xSpace*1), y+(ySpace*5)))
                pointsRight.append((x-(xSpace*2), y+(ySpace*6)))
                pointsRight.append((x-(xSpace*2), y+(ySpace*8)))
                pointsRight.append((x-(xSpace*3), y+(ySpace*9)))
                pointsRight.append((x-(xSpace*3), y+(ySpace*10)))

                pointsLeft = [
                    (pointsRight[-1][0]-(xSpace/2), pointsRight[-1][1])]

                for i in range(len(pointsRight)-2, -1, -1):
                    pointsLeft.append(
                        ((pointsRight[i][0]-(xSpace/2)), (pointsRight[i][1]-(ySpace/2))))
                pointsLeft[-1] = (pointsLeft[-1][0] +
                                  (xSpace/4), pointsLeft[-1][1]-(ySpace/4))
                points = pointsRight+pointsLeft
                self.__canvas.create_polygon(
                    points, fill="yellow", outline="black", width=3)

            def bottomRight(x, y):
                x = x-(xSpace*3)
                y = y+(ySpace*10)
                pointsRight = [(x, y),
                               (x, y+ySpace)]
                pointsRight.append((x+(xSpace*1), y+(ySpace*2)))
                pointsRight.append((x+(xSpace*1), y+(ySpace*4)))
                pointsRight.append((x+(xSpace*2), y+(ySpace*5)))
                pointsRight.append((x+(xSpace*2), y+(ySpace*7)))
                pointsRight.append((x+(xSpace*3), y+(ySpace*8)))
                pointsRight.append((x+(xSpace*3), y+(ySpace*10)))
                pointsRight.append((x+(xSpace*3.5), y+(ySpace*10.5)))

                pointsLeft = []
                for i in range(len(pointsRight)-1, -1, -1):
                    pointsLeft.append(
                        ((pointsRight[i][0]-(xSpace/2)), (pointsRight[i][1]+(ySpace/2))))

                pointsLeft[0] = (pointsLeft[0][0]+(xSpace/4),
                                 pointsLeft[0][1]+(ySpace/4))
                pointsLeft[-1] = (pointsLeft[-1][0],
                                  pointsLeft[-1][1]-(ySpace/2))

                points = pointsRight + pointsLeft
                self.__canvas.create_polygon(
                    points, fill="lime", outline="black", width=3)

            def topRight(x, y):
                x = x+(xSpace*8)
                pointsRight = [(x-(xSpace/2), y-(ySpace/2)),
                               (x, y)]
                pointsRight.append((x, y+(ySpace*2)))
                pointsRight.append((x+(xSpace*1), y+(ySpace*3)))
                pointsRight.append((x+(xSpace*1), y+(ySpace*5)))
                pointsRight.append((x+(xSpace*2), y+(ySpace*6)))
                pointsRight.append((x+(xSpace*2), y+(ySpace*8)))
                pointsRight.append((x+(xSpace*3), y+(ySpace*9)))
                pointsRight.append((x+(xSpace*3), y+(ySpace*10)))

                pointsLeft = [
                    (pointsRight[-1][0]+(xSpace/2), pointsRight[-1][1])]

                for i in range(len(pointsRight)-2, -1, -1):
                    pointsLeft.append(
                        ((pointsRight[i][0]+(xSpace/2)), (pointsRight[i][1]-(ySpace/2))))
                pointsLeft[-1] = (pointsLeft[-1][0] -
                                  (xSpace/4), pointsLeft[-1][1]-(ySpace/4))
                points = pointsRight+pointsLeft
                self.__canvas.create_polygon(
                    points, fill="lime", outline="black", width=3)

            def bottomLeft(x, y):
                x = x+(xSpace*11)
                y = y+(ySpace*10)
                pointsRight = [(x, y),
                               (x, y+ySpace)]
                pointsRight.append((x-(xSpace*1), y+(ySpace*2)))
                pointsRight.append((x-(xSpace*1), y+(ySpace*4)))
                pointsRight.append((x-(xSpace*2), y+(ySpace*5)))
                pointsRight.append((x-(xSpace*2), y+(ySpace*7)))
                pointsRight.append((x-(xSpace*3), y+(ySpace*8)))
                pointsRight.append((x-(xSpace*3), y+(ySpace*10)))
                pointsRight.append((x-(xSpace*3.5), y+(ySpace*10.5)))

                pointsLeft = []
                for i in range(len(pointsRight)-1, -1, -1):
                    pointsLeft.append(
                        ((pointsRight[i][0]+(xSpace/2)), (pointsRight[i][1]+(ySpace/2))))

                pointsLeft[0] = (pointsLeft[0][0]-(xSpace/4),
                                 pointsLeft[0][1]+(ySpace/4))
                pointsLeft[-1] = (pointsLeft[-1][0],
                                  pointsLeft[-1][1]-(ySpace/2))

                points = pointsRight + pointsLeft
                self.__canvas.create_polygon(
                    points, fill="yellow", outline="black", width=3)

            top(x, y)
            bottom(x, y)
            topLeft(x, y)
            topRight(x, y)
            bottomRight(x, y)
            bottomLeft(x, y)

        # Gets Grid
        grid = self.__table.getGrid()

        # Gets relative values for points generation
        xSpace = self.__cellSize
        ySpace = xSpace/2
        xCellSpace = xSpace
        yCellSpace = xSpace*1.50

        # Gets top left coords corner position, used to draw the border
        topLeftCoords = None

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col].getState() != 0:
                    x = (xCellSpace*col)+(xSpace)
                    y = (yCellSpace*row)+(ySpace*3)

                    # If topLeftCoords undefined, define.
                    if topLeftCoords == None:
                        topLeftCoords = (x, y)

                    backgroundHex(x, y, xSpace, ySpace)

                    mainHex()

        borders(topLeftCoords, xSpace, ySpace)

    def printCoords(self, event):
        print(event.x, event.y)


def run():
    win = rootWindow()


run()
