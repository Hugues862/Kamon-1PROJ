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
        
        xLast, yLast = self.__table.getLastCoord()
        
        if self.__table.getGrid()[y][x].getPlayer() == 0:
            if not self.__table.getGrid()[y][x].getSelected():
                self.__table.getGrid()[y][x].setSelected()
                
                if self.__table.getSelectedCoord() != None:
                    lastX, lastY = self.__table.getSelectedCoord()
                    self.__table.getGrid()[lastY][lastX].setSelected()
                self.__table.setSelectedCoord(x, y)
                
            elif self.__table.getGrid()[y][x].getSelected():
                
                if self.__table.getGrid()[yLast][xLast].color() == self.__table.getGrid()[y][x].color() or self.__table.getGrid()[yLast][xLast].getImage() == self.__table.getGrid()[y][x].getImage():
                    self.__table.getGrid()[y][x].setSelected()
                    self.__table.getGrid()[y][x].setLast()
                    self.__table.getGrid()[y][x].setPlayer(self.__turn + 1)
                    
                    if self.__table.getLastCoord() != None :
                        lastX, lastY = self.__table.getLastCoord()
                        self.__table.getGrid()[lastY][lastX].setLast()
                        self.__table.setLastCoord(x, y)
                
    def turnChange(self):
        self.__turn = (self.__turn + 1)  % 2
    
    def win(self):
        pass       
            
    def checkWin(self, x, y):
        neighbors, sides = self.__table.checkNeighbors(x, y, self.__turn):
    

        #Check if the 2 size colours exists
        if self.__turn== 0  or self.__turn == 1 :

            if ("G1" or "G1&Y1" or "G1&B1") and ("G2" or "G2&Y2" or "G2&B2") in sides:
                win()

            elif ("Y1" or "B2&Y1" or "G1&Y1") and ("Y2" or "B1&Y2" or "G2&Y2") in sides:
                win()

            elif ("B1" or "G1&B1" or"G1&Y1") and ("B2" or "B2&Y1" or "G2&B2") in sides:
                win()
            
        #Check if there a un boucle for the condition of win 
        # for self.checkNeighbors() in range(self.__table.getGrid()[y][x]):
            

            
        

        
                
            
            

def createGame():
    return Game()
