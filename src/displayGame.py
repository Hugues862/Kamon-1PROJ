import pickle
import threading
import commun.table
import commun.game
import win
import socket
import tkinter as tk
from PIL import Image, ImageTk
import pathlib
import logging
from commun.network import *

logging.basicConfig(level=logging.INFO)

WorkingDirectory = pathlib.Path().resolve()
TB = 2048 * 4


class rootWindow:
    def __init__(self, version, s=None, conn=None, addr=None):
        self.version = version  # solo (v1), server (v2), bot (v3)
        self.s = s
        self.conn = conn
        self.addr = addr
        if self.version == "server":
            self.id = pickle.loads(self.s.recv(TB))
            logging.info(f"Received ID from server | {self.id}")

        # Default cell size
        self.__cellSize = 60

        self.__indexx = 0
        self.__indexy = 0

        # Init tkinter stuff
        self.tkInit()

        # Generate new table
        if self.version == "solo" or self.version == "bot":
            self.__game = commun.game.createGame()
        elif self.version == "server":
            self.__game = pickle.loads(self.s.recv(TB)).game
            logging.info(f"Received self.__game from server | {self.__game}")

            # create server listening threading
            self.listeningThread = threading.Thread(target=self.listeningThreadFunction)
            self.listeningThread.start()

        # main loop
        self.updateDisplay()
        self.__root.mainloop()

    def listeningThreadFunction(self):
        while True:
            data = recv_data(self.s)
            stock = pickle.loads(data)
            self.__game = stock.game
            self.updateDisplay()

    def tkInit(self):
        """
        Init of tkinter elements
        """
        self.__root = tk.Tk()
        self.__width = self.__root.winfo_screenwidth()
        self.__height = self.__root.winfo_screenheight()
        self.__root.config(width=self.__width, height=self.__height)

        self.__frame = tk.Frame(self.__root, background="black")
        self.__frame.config(width=self.__width, height=self.__height)
        self.__frame.grid(row=0, column=0)
        self.__canvas = tk.Canvas(self.__frame)
        self.__canvas.config(
            width=(self.__cellSize * 16),
            height=(self.__cellSize * 13),
            highlightthickness=0,
            bd=0,
            bg="white",
        )
        self.__canvas.bind("<Button-1>", self.mouseClick)
        self.hexImages = {}

    def updateDisplay(self):

        # Display Game
        self.displayHex()

        # Update Game
        # self.__game.updateGame()

        # TK packing
        self.__canvas.pack()

    def displayHex(self):
        def hex(x, y, xSpace, ySpace, hexObject, col, row):
            color = hexObject.getColor()
            player = hexObject.getPlayer()
            last = hexObject.getLast()
            selected = hexObject.getSelected()
            state = hexObject.getState()
            imagePath = hexObject.getImage()

            """Displays Background Canvas and generates points"""
            points = [
                (x, y),
                (x + xSpace, y - ySpace),
                (x + (xSpace * 2), y),
                (x + (xSpace * 2), y + (2 * ySpace)),
                (x + xSpace, y + (3 * ySpace)),
                (x, y + (2 * ySpace)),
            ]

            mx = self.__root.winfo_pointerx() - self.__root.winfo_rootx()
            my = self.__root.winfo_pointery() - self.__root.winfo_rooty()
            if self.findPointsInsidePolygon(mx, my, points):
                self.__indexx = col
                self.__indexy = row

            if last:
                mainHex(points, color, "gold", imagePath)
            elif player == 1:
                mainHex(points, color, "black", imagePath)
            elif player == 2:
                mainHex(points, color, "white", imagePath)
            elif selected:
                mainHex(points, color, "red", imagePath)
            else:
                self.__canvas.create_polygon(
                    points, fill=color, outline="black", width=2
                )

        def mainHex(points, color, border, imagePath):
            """Displays the hexagones on the cells ( basically displays the players )"""
            # Polygon
            # FILL WHITE = BORDER
            self.__canvas.create_polygon(points, fill=border, outline="black", width=3)
            # Rayon
            rx = xSpace * 0.75
            ry = ySpace * 1.25
            # Circle
            xlist = [point[0] for point in points]
            ylist = [point[1] for point in points]
            x = (sum(xlist) / len(points)) - rx
            y = (sum(ylist) / len(points)) - ry

            # FILL COLOR = Cell original color
            self.__canvas.create_oval(
                x,
                y,
                x + (xSpace * 1.5),
                y + (ySpace * 2.5),
                fill=color,
                outline="black",
                width=3,
            )

        def borders(*args):
            """Displays the borders"""
            x, y = topLeftCoords

            def top(x, y):
                xspace2 = xSpace / 2
                yspace2 = ySpace / 2

                pointsBottom = [(x + xspace2, y - yspace2), (x + xSpace, y - ySpace)]
                for i in range(2, 7, 2):
                    pointsBottom.append((x + (xSpace * i), y))
                    pointsBottom.append((x + (xSpace * (i + 1)), y - ySpace))
                pointsBottom.append((x + (xSpace * 7.5), y - yspace2))

                pointsTop = []
                for i in range(len(pointsBottom) - 1, -1, -1):
                    pointsTop.append(
                        (pointsBottom[i][0], (pointsBottom[i][1] - (ySpace)))
                    )
                xspace4 = xSpace / 4
                yspace4 = ySpace / 4
                pointsTop[0] = (
                    pointsTop[0][0] + (xspace4),
                    pointsTop[0][1] + (yspace4),
                )
                pointsTop[-1] = (
                    pointsTop[-1][0] - (xspace4),
                    pointsTop[-1][1] + (yspace4),
                )

                points = pointsBottom + pointsTop
                self.__canvas.create_polygon(
                    points, fill="cyan", outline="black", width=3
                )

            def bottom(x, y):
                y = y + (ySpace * 22)
                pointsBottom = [(x + (xSpace / 2), y - (ySpace / 2)), (x + xSpace, y)]
                for i in range(2, 7, 2):
                    pointsBottom.append((x + (xSpace * i), y - ySpace))
                    pointsBottom.append((x + (xSpace * (i + 1)), y))
                pointsBottom.append((x + (xSpace * 7.5), y - (ySpace / 2)))

                pointsTop = []
                for i in range(len(pointsBottom) - 1, -1, -1):
                    pointsTop.append(
                        (pointsBottom[i][0], (pointsBottom[i][1] - (ySpace)))
                    )

                pointsBottom[0] = (
                    pointsBottom[0][0] - (xSpace / 4),
                    pointsBottom[0][1] - (ySpace / 4),
                )
                pointsBottom[-1] = (
                    pointsBottom[-1][0] + (xSpace / 4),
                    pointsBottom[-1][1] - (ySpace / 4),
                )

                points = pointsBottom + pointsTop
                self.__canvas.create_polygon(
                    points, fill="cyan", outline="black", width=3
                )

            def topLeft(x, y):
                pointsRight = [(x + (xSpace / 2), y - (ySpace / 2)), (x, y)]
                pointsRight.append((x, y + (ySpace * 2)))
                pointsRight.append((x - (xSpace * 1), y + (ySpace * 3)))
                pointsRight.append((x - (xSpace * 1), y + (ySpace * 5)))
                pointsRight.append((x - (xSpace * 2), y + (ySpace * 6)))
                pointsRight.append((x - (xSpace * 2), y + (ySpace * 8)))
                pointsRight.append((x - (xSpace * 3), y + (ySpace * 9)))
                pointsRight.append((x - (xSpace * 3), y + (ySpace * 10)))

                pointsLeft = [(pointsRight[-1][0] - (xSpace / 2), pointsRight[-1][1])]

                for i in range(len(pointsRight) - 2, -1, -1):
                    pointsLeft.append(
                        (
                            (pointsRight[i][0] - (xSpace / 2)),
                            (pointsRight[i][1] - (ySpace / 2)),
                        )
                    )
                pointsLeft[-1] = (
                    pointsLeft[-1][0] + (xSpace / 4),
                    pointsLeft[-1][1] - (ySpace / 4),
                )
                points = pointsRight + pointsLeft
                self.__canvas.create_polygon(
                    points, fill="yellow", outline="black", width=3
                )

            def bottomRight(x, y):
                x = x - (xSpace * 3)
                y = y + (ySpace * 10)
                pointsRight = [(x, y), (x, y + ySpace)]
                pointsRight.append((x + (xSpace * 1), y + (ySpace * 2)))
                pointsRight.append((x + (xSpace * 1), y + (ySpace * 4)))
                pointsRight.append((x + (xSpace * 2), y + (ySpace * 5)))
                pointsRight.append((x + (xSpace * 2), y + (ySpace * 7)))
                pointsRight.append((x + (xSpace * 3), y + (ySpace * 8)))
                pointsRight.append((x + (xSpace * 3), y + (ySpace * 10)))
                pointsRight.append((x + (xSpace * 3.5), y + (ySpace * 10.5)))

                pointsLeft = []
                for i in range(len(pointsRight) - 1, -1, -1):
                    pointsLeft.append(
                        (
                            (pointsRight[i][0] - (xSpace / 2)),
                            (pointsRight[i][1] + (ySpace / 2)),
                        )
                    )

                pointsLeft[0] = (
                    pointsLeft[0][0] + (xSpace / 4),
                    pointsLeft[0][1] + (ySpace / 4),
                )
                pointsLeft[-1] = (pointsLeft[-1][0], pointsLeft[-1][1] - (ySpace / 2))

                points = pointsRight + pointsLeft
                self.__canvas.create_polygon(
                    points, fill="lime", outline="black", width=3
                )

            def topRight(x, y):
                x = x + (xSpace * 8)
                pointsRight = [(x - (xSpace / 2), y - (ySpace / 2)), (x, y)]
                pointsRight.append((x, y + (ySpace * 2)))
                pointsRight.append((x + (xSpace * 1), y + (ySpace * 3)))
                pointsRight.append((x + (xSpace * 1), y + (ySpace * 5)))
                pointsRight.append((x + (xSpace * 2), y + (ySpace * 6)))
                pointsRight.append((x + (xSpace * 2), y + (ySpace * 8)))
                pointsRight.append((x + (xSpace * 3), y + (ySpace * 9)))
                pointsRight.append((x + (xSpace * 3), y + (ySpace * 10)))

                pointsLeft = [(pointsRight[-1][0] + (xSpace / 2), pointsRight[-1][1])]

                for i in range(len(pointsRight) - 2, -1, -1):
                    pointsLeft.append(
                        (
                            (pointsRight[i][0] + (xSpace / 2)),
                            (pointsRight[i][1] - (ySpace / 2)),
                        )
                    )
                pointsLeft[-1] = (
                    pointsLeft[-1][0] - (xSpace / 4),
                    pointsLeft[-1][1] - (ySpace / 4),
                )
                points = pointsRight + pointsLeft
                self.__canvas.create_polygon(
                    points, fill="lime", outline="black", width=3
                )

            def bottomLeft(x, y):
                x = x + (xSpace * 11)
                y = y + (ySpace * 10)
                pointsRight = [(x, y), (x, y + ySpace)]
                pointsRight.append((x - (xSpace * 1), y + (ySpace * 2)))
                pointsRight.append((x - (xSpace * 1), y + (ySpace * 4)))
                pointsRight.append((x - (xSpace * 2), y + (ySpace * 5)))
                pointsRight.append((x - (xSpace * 2), y + (ySpace * 7)))
                pointsRight.append((x - (xSpace * 3), y + (ySpace * 8)))
                pointsRight.append((x - (xSpace * 3), y + (ySpace * 10)))
                pointsRight.append((x - (xSpace * 3.5), y + (ySpace * 10.5)))

                pointsLeft = []
                for i in range(len(pointsRight) - 1, -1, -1):
                    pointsLeft.append(
                        (
                            (pointsRight[i][0] + (xSpace / 2)),
                            (pointsRight[i][1] + (ySpace / 2)),
                        )
                    )

                pointsLeft[0] = (
                    pointsLeft[0][0] - (xSpace / 4),
                    pointsLeft[0][1] + (ySpace / 4),
                )
                pointsLeft[-1] = (pointsLeft[-1][0], pointsLeft[-1][1] - (ySpace / 2))

                points = pointsRight + pointsLeft
                self.__canvas.create_polygon(
                    points, fill="yellow", outline="black", width=3
                )

            top(x, y)
            bottom(x, y)
            topLeft(x, y)
            topRight(x, y)
            bottomRight(x, y)
            bottomLeft(x, y)

        def images(x, y, xSpace, ySpace, gridElem):
            imagePath = gridElem.getImage()

            if imagePath != None:
                # not loaded

                if imagePath not in self.hexImages.keys():
                    imgUrl = str(str(WorkingDirectory) + imagePath)
                    image = Image.open(imgUrl)
                    mult = 1.2
                    ns = (round(xSpace * mult), round(ySpace * mult * 2))
                    image = image.resize(
                        ns,
                    )
                    img = ImageTk.PhotoImage(image)
                    self.hexImages[imagePath] = img
                    self.__canvas.image_names = list(self.hexImages.values())
                # loaded
                else:
                    img = self.hexImages[imagePath]

                self.__canvas.create_image(
                    x + xSpace,
                    y + ySpace,
                    image=img,
                )

        # Gets Grid
        grid = self.__game.getTable().getGrid()

        # Gets relative values for points generation
        xSpace = self.__cellSize
        ySpace = xSpace / 2
        xCellSpace = xSpace
        yCellSpace = xSpace * 1.50

        # Gets top left coords corner position, used to draw the border
        topLeftCoords = None

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col].getState() != 0:
                    x = (xCellSpace * col) + (xSpace)
                    y = (yCellSpace * row) + (ySpace * 3)

                    # If topLeftCoords undefined, define.
                    if topLeftCoords == None:
                        topLeftCoords = (x, y)

                    hex(
                        x=x,
                        y=y,
                        xSpace=xSpace,
                        ySpace=ySpace,
                        hexObject=grid[row][col],
                        col=col,
                        row=row,
                    )
                    images(
                        x=x, y=y, xSpace=xSpace, ySpace=ySpace, gridElem=grid[row][col]
                    )

        borders(topLeftCoords, xSpace, ySpace)

    def mouseClick(self, event):
        # x, y = self.pixelToIndex(event.x, event.y)
        # print(event.x, event.y)
        self.updateDisplay()
        selected = self.__game.mouseClick(self.__indexx, self.__indexy, self.version)
        if self.version == "server" and selected == True:
            data = pickle.dumps(self.__game)
            send_data(self.s, data)
        self.updateDisplay()

        """  if self.__game.getWin():
            self.win() """

    def findPointsInsidePolygon(self, x, y, poly):
        n = len(poly)
        inside = False

        p1x, p1y = poly[0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    # def pixelToIndex(self, xPix, yPix):
    # return 3, 6

    def win(self):
        self.__root.destroy()
        win.winRun(self.__game.getTurn())
        # self.__root.destroy() # For debug and understanding win conditions


def gameRun(version, s = None, conn = None, addr = None):
    
    if version == "solo" or version == "bot":
        game = rootWindow(version)

    if version == "server":
        
        HOST = "localhost"
        PORT = 56669
        # creating client
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            logging.info(f"Attempting to connect to server {HOST}:{PORT}")
            s.connect((HOST, PORT))
            logging.info(f"Connected")
            game = rootWindow(version=version, s=s)


# gameRun("solo")
# gameRun("server")
# gameRun("bot")
