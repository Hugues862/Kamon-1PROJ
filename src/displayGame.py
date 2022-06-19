import pathlib
import logging
import threading

import tkinter as tk
from PIL import Image, ImageTk

import socket
import pickle
from commun.network import *

import commun.table
import commun.game
import win


logging.basicConfig(level=logging.INFO)

WorkingDirectory = pathlib.Path().resolve()
TB = 2048 * 4


class rootWindow:
    def __init__(
        self,
        version,
        s=None,
        conn=None,
        addr=None,
        p1="Player",
        p2="Bot",
        theme="original",
    ):
        """Initialize a new window to display the game.

        Args:
            version (str): solo, bot or server. Game will act differently depending on the version.
            s (socket, optional): Socket to connect to. Defaults to None.
            conn (str, optional): Ip of the server. Defaults to None.
            addr (str, optional): Ip of the client. Defaults to None.
            p1 (str, optional): Name of Player 1. Defaults to "Player".
            p2 (str, optional): Name of Player 2. Defaults to "Bot".
            theme (str, optional): Theme of the game. Defaults to "original".
        """

        self.version = version  # ? solo (v1), server (v2), bot (v3)
        self.s = s
        self.conn = conn
        self.addr = addr

        # ! Window receives an ID from the server if version == server
        if self.version == "server":
            self.id = pickle.loads(self.s.recv(TB))
            logging.info(f"Received ID from server | {self.id}")

        self.__cellSize = 60

        self.__indexx = 0
        self.__indexy = 0

        # ! Initialize the window
        self.tkInit()

        # ! Generate a new game object or receives the game object from the server

        if self.version == "solo" or self.version == "bot":
            self.__game = commun.game.createGame(p1, p2, theme)
        elif self.version == "server":
            self.__game = pickle.loads(self.s.recv(TB)).game
            logging.info(f"Received self.__game from server | {self.__game}")

            # ! Creates a listening Thread to stay updated with the server

            self.listeningThread = threading.Thread(target=self.listeningThreadFunction)
            self.listeningThread.start()

        # ! Start the main loop of the game
        self.updateDisplay()
        self.__root.mainloop()

    def listeningThreadFunction(self):
        """Listening thread constantly updating the display and self.__game with the server data."""

        while True:
            data = recv_data(self.s)
            stock = pickle.loads(data)
            self.__game = stock.game
            self.updateDisplay()

    def tkInit(self):
        """Initialize the tkinter base window."""

        self.__root = tk.Tk()
        self.__root.title("KAMON")
        self.__width = self.__root.winfo_screenwidth()
        self.__height = self.__root.winfo_screenheight()
        self.__root.config(width=self.__width, height=self.__height)

        self.__frame = tk.Frame(self.__root, background="black")
        self.__frame.config(width=self.__width, height=self.__height)
        self.__frame.grid(row=0, column=0)

        # * Initialize the canvas to draw on
        self.__canvas = tk.Canvas(self.__frame)
        self.__canvas.config(
            width=(self.__cellSize * 16),
            height=(self.__cellSize * 13),
            highlightthickness=0,
            bd=0,
            bg="white",
        )

        # ! Binds the left mouse click to the mouseClick function
        self.__canvas.bind("<Button-1>", self.mouseClick)
        self.hexImages = {}

    def updateDisplay(self):
        """_summary_"""

        # * Display Game
        self.displayHex()
        self.displayTurn()

        # TK packing
        self.__canvas.pack()

    def displayHex(self):
        """Displays the entire grid of hexagons using local functions."""

        def hex(x, y, xSpace, ySpace, hexObject, col, row):

            color = hexObject.getColor()
            player = hexObject.getPlayer()
            last = hexObject.getLast()
            selected = hexObject.getSelected()
            imagePath = hexObject.getImage()

            # * Generates points of the current hexagon
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

            # * Draws the current hexagon on the canvas depending on its variables

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
            """Draws a hexagon on the canvas with its properties"""

            # ? Polygon
            self.__canvas.create_polygon(points, fill=border, outline="black", width=3)

            # ? Radius
            rx = xSpace * 0.75
            ry = ySpace * 1.25

            # ? Circle
            xlist = [point[0] for point in points]
            ylist = [point[1] for point in points]
            x = (sum(xlist) / len(points)) - rx
            y = (sum(ylist) / len(points)) - ry

            # * Draws the "KAMON" on top of the hexagon
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
            """Display the image of current hexagon"""

            imagePath = gridElem.getImage()

            # * If image not loaded yet
            if imagePath != None:

                if imagePath not in self.hexImages.keys():

                    #  ? Get the image path
                    imgUrl = str(str(WorkingDirectory) + imagePath)
                    image = Image.open(imgUrl)

                    # ? Resize the image
                    mult = 1.2
                    ns = (round(xSpace * mult), round(ySpace * mult * 2))
                    image = image.resize(
                        ns,
                    )

                    # ? Load the image
                    img = ImageTk.PhotoImage(image)
                    self.hexImages[imagePath] = img
                    self.__canvas.image_names = list(self.hexImages.values())

                # * If image already loaded
                else:
                    img = self.hexImages[imagePath]

                # ? Display the image on the canvas
                self.__canvas.create_image(
                    x + xSpace,
                    y + ySpace,
                    image=img,
                )

        # * Get the game grid
        grid = self.__game.getTable().getGrid()

        # * Gets relative values for points generation
        xSpace = self.__cellSize
        ySpace = xSpace / 2
        xCellSpace = xSpace
        yCellSpace = xSpace * 1.50

        # * Gets top left coords corner position, used to draw the border
        topLeftCoords = None

        # ! For every cell in grid draw the hex accordingly if not empty cell (state == 0)
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

        # ? Draws the borders of the board
        borders(topLeftCoords, xSpace, ySpace)

    def displayTurn(self):
        """Displays the name of the current player."""

        # ? Get current player's name to display turn
        game = self.__game
        turn = game.getTurn()
        turnText = game.getPlayer(turn).name + "'s turn"

        self.__turnFrame = tk.Frame(self.__frame, bg="white", width=100, height=100)
        self.__turnFrame.place(x=5, y=5)

        turnLabel = tk.Label(self.__turnFrame, text=turnText, bg="white")
        turnLabel.config(font=("Big John PRO", 15))
        turnLabel.pack()

    def mouseClick(self, event):
        """Change the hex values according to the mouse position.

        Args:
            event (event): tkinter Event.
        """

        # ? Refresh canvas
        self.updateDisplay()

        # ! Change the board state then send data to server
        if self.version == "server":
            self.__game.mouseClick(
                self.__indexx, self.__indexy, self.version, playerId=self.id
            )
            data = pickle.dumps(self.__game)
            send_data(self.s, data)

        # ! Change the board state
        else:
            self.__game.mouseClick(self.__indexx, self.__indexy, self.version)

        # ? Refresh the canvas again to see change
        self.updateDisplay()

        if self.__game.getWin():
            self.win()

    def findPointsInsidePolygon(self, x, y, poly):
        """Checks if mouse is inside a polygon .

        Args:
            x (int): x index of the current point in array.
            y (_type_): _description_
            poly (_type_): _description_

        Returns:
            bool: If mouse is inside a polygon.
        """

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
        winner = self.__game.getTurn()
        win.startWin(self.__game.getPlayer(winner).name)
        # self.__root.destroy() # For debug and understanding win conditions


def startGame(
    version, s=None, server_ip="localhost", p1="Player", p2="Bot", theme="original"
):

    if version == "solo" or version == "bot":
        game = rootWindow(version=version, p1=p1, p2=p2, theme=theme)

    if version == "server":

        HOST = server_ip
        PORT = 56669
        # creating client
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            logging.info(f"Attempting to connect to server {HOST}:{PORT}")
            s.connect((HOST, PORT))
            logging.info(f"Connected")
            game = rootWindow(version=version, s=s, theme=theme)


# startGame("solo")
# startGame("server")
# startGame("bot")
