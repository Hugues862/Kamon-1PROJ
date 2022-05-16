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
        
        xLast, yLast = self.__table.getLastCoord()
        
        if grid[y][x].getPlayer() == 0:
            if not grid[y][x].getSelected():
                grid[y][x].setSelected()
                
        
        if grid[y][x].getPlayer() == 0:
            if not grid[y][x].getSelected():
                grid[y][x].setSelected()

                if self.__table.getSelectedCoord() != None:
                    lastX, lastY = self.__table.getSelectedCoord()
                    grid[lastY][lastX].setSelected()
                self.__table.setSelectedCoord(x, y)
                
            elif grid[y][x].getSelected():
                
                if grid[yLast][xLast].color() == grid[y][x].color() or grid[yLast][xLast].getImage() == grid[y][x].getImage():
                    grid[y][x].setSelected()
                    grid[y][x].setLast()
                    grid[y][x].setPlayer(self.__turn + 1)
                    
                    if self.__table.getLastCoord() != None :
                        lastX, lastY = self.__table.getLastCoord()
                        grid[lastY][lastX].setLast()
                        self.__table.setLastCoord(x, y)
                
    def turnChange(self):
        self.__turn = (self.__turn + 1)  % 2
    
    def win(self):
        pass       
            
    def checkWin(self, x, y):
        
        neighbors, sides = self.__table.checkNeighbors(x, y, self.__turn)
        grid = self.__table.getGrid()

        #Check if the 2 size colours exists
        if self.__turn== 0  or self.__turn == 1 :

            if ("G1" or "G1&Y1" or "G1&B1") and ("G2" or "G2&Y2" or "G2&B2") in sides:
                self.win()

            elif ("Y1" or "B2&Y1" or "G1&Y1") and ("Y2" or "B1&Y2" or "G2&Y2") in sides:
                self.win()

            elif ("B1" or "G1&B1" or"G1&Y1") and ("B2" or "B2&Y1" or "G2&B2") in sides:
                self.win()
            
        #Check if there a un boucle for the condition of win 
        # for self.checkNeighbors() in range(self.__table.getGrid()[y][x]):
        
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
