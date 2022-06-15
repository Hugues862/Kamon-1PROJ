import commun.table
import random as rd

# import win


class Player:
    def __init__(self, color, name):
        self.name = name
        self.kamons = 18
        self.color = color
        self.playerLast = None


class Game:
    def __init__(self, p1, p2):
        self.__table = commun.table.Table()
        self.__players = [Player("black", p1), Player("white", p2)]
        self.__turn = 0  # Black starts
        self.__win = False

    def getTable(self):
        return self.__table

    def getTurn(self):
        return self.__turn

    def getWin(self):
        return self.__win

    def getPlayer(self, player):

        return self.__players[player - 1]

    # def updateGame(self):
    #     pass

    def place(self, x, y):

        grid = self.__table.getGrid()

        grid[y][x].setLast()
        self.__players[self.__turn].playerLast = (x, y)
        grid[y][x].setPlayer(self.__turn + 1)

        if self.__table.getLastCoord() != None:
            lastX, lastY = self.__table.getLastCoord()
            grid[lastY][lastX].setLast()  # Removes Last status from last ring

        self.__table.setLastCoord(x, y)

        if self.checkWin(x, y) == True:
            self.__win = True
        else:
            self.turnChange()

    def mouseClick(self, x, y, version):

        grid = self.__table.getGrid()

        # if grid[y][x].getPlayer() == 0:
        #     if not grid[y][x].getSelected():
        #         grid[y][x].setSelected()

        if grid[y][x].getState() != 0 and grid[y][x].getPlayer() == 0:
            if not grid[y][x].getSelected():
                grid[y][x].setSelected()

                if self.__table.getSelectedCoord() != None:
                    selectX, selectY = self.__table.getSelectedCoord()
                    grid[selectY][selectX].setSelected()
                self.__table.setSelectedCoord(x, y)
                return False

            elif grid[y][x].getSelected() and grid[y][x].getState() != -1:

                if self.__table.isPossible(x, y):
                    grid[y][x].setSelected()
                    self.place(x, y)

                    if version == "bot" and self.__win == False:
                        self.aiBot()

                return True
        return False

    def turnChange(self):
        self.__turn = (self.__turn + 1) % 2

    def checkWin(self, x, y):

        if self.allPossible() == []:
            return True

        side = self.__table.checkNeighbors(x, y, self.__turn, [], [])[1]
        # print(side)

        grid = self.__table.getGrid()

        # Check if the 2 side colours exists

        if ("G1" in side or "B1&G1" in side or "G1&Y2" in side) and (
            "G2" in side or "B2&G2" in side or "G2&Y1" in side
        ):
            # print("color1")
            return True

        elif ("Y1" in side or "B1&Y1" in side or "G2&Y1" in side) and (
            "Y2" in side or "B2&Y2" in side or "G1&Y2" in side
        ):
            # print("color2")
            return True

        elif ("B1" in side or "G1&B1" in side or "B1&G1" in side) and (
            "B2" in side or "B2&G2" in side or "B2&Y2" in side
        ):
            # print("color3")
            return True

        if (
            x != abs(3 - y)
            and grid[y][x - 2].getState() != 0
            and (
                grid[y][x - 2].getPlayer() == 2 - self.__turn
                or grid[y][x - 2].getPlayer() == 0
            )
        ):
            winSides = self.__table.checkWinNeighbors(x - 2, y, self.__turn, [], [])[1]
            if all(side is None for side in winSides):
                # print("surround1")
                return True

        if (
            x != 12 - abs(3 - y)
            and grid[y][x + 2].getState() != 0
            and (
                grid[y][x + 2].getPlayer() == 2 - self.__turn
                or grid[y][x + 2].getPlayer() == 0
            )
        ):
            winSides = self.__table.checkWinNeighbors(x + 2, y, self.__turn, [], [])[1]
            if all(side is None for side in winSides):
                # print("surround2")
                return True

        if (
            y != 0
            and grid[y - 1][x + 1].getState() != 0
            and (
                grid[y - 1][x + 1].getPlayer() == 2 - self.__turn
                or grid[y - 1][x + 1].getPlayer() == 0
            )
        ):
            winSides = self.__table.checkWinNeighbors(
                x + 1, y - 1, self.__turn, [], []
            )[1]
            if all(side is None for side in winSides):
                # print("surround3")
                return True

        if (
            y != 0
            and grid[y - 1][x - 1].getState() != 0
            and (
                grid[y - 1][x - 1].getPlayer() == 2 - self.__turn
                or grid[y - 1][x - 1].getPlayer() == 0
            )
        ):
            winSides = self.__table.checkWinNeighbors(
                x - 1, y - 1, self.__turn, [], []
            )[1]
            if all(side is None for side in winSides):
                # print("surround4")
                return True

        if (
            y != 6
            and grid[y + 1][x + 1].getState() != 0
            and (
                grid[y + 1][x + 1].getPlayer() == 2 - self.__turn
                or grid[y + 1][x + 1].getPlayer() == 0
            )
        ):
            winSides = self.__table.checkWinNeighbors(
                x + 1, y + 1, self.__turn, [], []
            )[1]
            if all(side is None for side in winSides):
                # print("surround5")
                return True

        if (
            y != 6
            and grid[y + 1][x - 1].getState() != 0
            and (
                grid[y + 1][x - 1].getPlayer() == 2 - self.__turn
                or grid[y + 1][x - 1].getPlayer() == 0
            )
        ):
            winSides = self.__table.checkWinNeighbors(
                x - 1, y + 1, self.__turn, [], []
            )[1]
            if all(side is None for side in winSides):
                # print("surround6")
                return True

        return False

    # AI BOT

    def allPossible(self):

        res = []

        for y in range(7):
            for x in range(7 - abs(3 - y)):

                if self.__table.isPossible(abs(3 - y) + (x * 2), y):
                    res.append((abs(3 - y) + (x * 2), y))

        return res

    def aiBot(self):

        available = self.allPossible()

        pos = None  # (x, y) used by the AI bot
        nbrNeighbors = 0

        # Try to put next to ally pieces
        for idx in range(len(available)):

            tmp = len(
                self.__table.checkNeighbors(
                    available[idx][0], available[idx][1], self.__turn, [], []
                )[0]
            )

            if tmp > nbrNeighbors:
                nbrNeighbors = tmp
                pos = available[idx]

        # If ally pieces not enough, try to put next to enemy last piece
        if nbrNeighbors <= 3 and self.__table.getLastCoord() != None:

            lastX, lastY = self.__table.getLastCoord()

            if (lastX - 2, lastY) in available:
                pos = (lastX - 2, lastY)

            elif (lastX + 2, lastY) in available:
                pos = (lastX + 2, lastY)

            elif (lastX - 1, lastY - 1) in available:
                pos = (lastX - 1, lastY - 1)

            elif (lastX + 1, lastY - 1) in available:
                pos = (lastX + 1, lastY - 1)

            elif (lastX - 1, lastY + 1) in available:
                pos = (lastX - 1, lastY + 1)

            elif (lastX + 1, lastY + 1) in available:
                pos = (lastX + 1, lastY + 1)

            else:
                pos = available[rd.randint(0, len(available) - 1)]

        # If no previous piece, play random
        else:
            pos = available[rd.randint(0, len(available) - 1)]

        # Place piece on posX, posY
        self.place(pos[0], pos[1])


def createGame(p1="Player1", p2="Player2"):
    return Game(p1, p2)
