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

    def mouseClick(self):
        pass


def createGame():
    return Game()
