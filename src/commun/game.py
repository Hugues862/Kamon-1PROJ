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
        if self.__table.getGrid()[y][x].getPlayer() == 0:
            if not self.__table.getGrid()[y][x].getSelected():
                self.__table.getGrid()[y][x].setSelected()
                
                if self.__table.getSelectedCoord() != None:
                    lastX, lastY = self.__table.getSelectedCoord()
                    self.__table.getGrid()[lastY][lastX].setSelected()
                self.__table.setSelectedCoord(x, y)
                
            elif self.__table.getGrid()[y][x].getSelected():
                
                self.__table.getGrid()[y][x].setSelected()
                self.__table.getGrid()[y][x].setLast()
                self.__table.getGrid()[y][x].setPlayer(self.__turn + 1)
                
                if self.__table.getLastCoord() != None :
                    lastX, lastY = self.__table.getLastCoord()
                    self.__table.getGrid()[lastY][lastX].setLast()
                self.__table.setLastCoord(x, y)
            
            
            
            


def createGame():
    return Game()
