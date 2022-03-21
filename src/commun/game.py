import commun.table


class Player:
    def __init__(self, color):
        self.kamons = 18
        self.color = color


class Game:
    def __init__(self):
        self.__table = commun.table.Table()
        self.__players = [Player("black"), Player("white")]
        self.__turn = 0  # Black starts

    def getTable(self):
        return self.__table

    def updateGame(self):
        pass

    def mouseClick(self, x, y):
        grid = self.__table.getGrid()
        if grid[y][x].getPlayer() == 0:
            if not grid[y][x].getSelected():
                grid[y][x].setSelected()

                if self.__table.getSelectedCoord() != None:
                    lastX, lastY = self.__table.getSelectedCoord()
                    grid[lastY][lastX].setSelected()
                self.__table.setSelectedCoord(x, y)

            elif grid[y][x].getSelected():

                grid[y][x].setSelected()
                grid[y][x].setLast()
                grid[y][x].setPlayer(self.__turn + 1)

                if self.__table.getLastCoord() != None:
                    lastX, lastY = self.__table.getLastCoord()
                    grid[lastY][lastX].setLast()
                self.__table.setLastCoord(x, y)


def createGame():
    return Game()
