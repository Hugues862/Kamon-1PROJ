import commun.table
# import win


class Player:
    def __init__(self, color):
        self.kamons = 18
        self.color = color


class Game:
    def __init__(self):
        self.__table = commun.table.Table()
        self.__players = [Player("black"), Player("white")]
        self.__turn = 0  # Black starts
        self.__win = False

    def getTable(self):
        return self.__table
    
    def getTurn(self):
        return self.__turn
    
    def getWin(self):
        return self.__win

    # def updateGame(self):
    #     pass

    def mouseClick(self, x, y):
        
        grid = self.__table.getGrid()
        
        if self.__table.getLastCoord() != None:
            lastX, lastY = self.__table.getLastCoord()
        
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
                
            elif grid[y][x].getSelected() and grid[y][x].getState() != -1:
                
                if self.__table.getLastCoord() == None or grid[lastY][lastX].getColor() == grid[y][x].getColor() or grid[lastY][lastX].getImage() == grid[y][x].getImage():
                    grid[y][x].setSelected()
                    grid[y][x].setLast()
                    grid[y][x].setPlayer(self.__turn + 1)
                    
                    if self.__table.getLastCoord() != None :
                        grid[lastY][lastX].setLast() # Removes Lest status from last ring
                        
                    self.__table.setLastCoord(x, y)
                    if self.checkWin(x, y) == True:
                        self.__win = True
                    else:    
                        self.turnChange()
                
    def turnChange(self):
        self.__turn = (self.__turn + 1)  % 2

    
           
            
    def checkWin(self, x, y):
        
        sides = self.__table.checkNeighbors(x, y, self.__turn)[1]
        grid = self.__table.getGrid()

        #Check if the 2 side colours exists
        # if self.__turn == 0  or self.__turn == 1 :

        if ("G1" or "G1&Y1" or "G1&B1") and ("G2" or "G2&Y2" or "G2&B2") in sides:
             return True

        elif ("Y1" or "B2&Y1" or "G1&Y1") and ("Y2" or "B1&Y2" or "G2&Y2") in sides:
            return True

        elif ("B1" or "G1&B1" or"B1&Y2") and ("B2" or "B2&Y1" or "G2&B2") in sides:
            return True
        
        if x != 0 and grid[y][x - 2].getState() != 0 and (grid[y][x - 2].getPlayer() == 2 - self.__turn or grid[y][x - 2].getPlayer() == 0):
            winSides = self.__table.checkWinNeighbors(x - 2, y, self.__turn)[1]
            if all(side is None for side in winSides):
                return True
                
        if x != 12 and grid[y][x + 2].getState() != 0 and (grid[y][x + 2].getPlayer() == 2 - self.__turn or grid[y][x + 2].getPlayer() == 0):
            winSides = self.__table.checkWinNeighbors(x + 2, y, self.__turn)[1]
            if all(side is None for side in winSides):
                return True
                
        if y != 0 and grid[y - 1][x + 1].getState() != 0 and (grid[y - 1][x + 1].getPlayer() == 2 - self.__turn or grid[y - 1][x + 1].getPlayer() == 0):
            winSides = self.__table.checkWinNeighbors(x + 1, y - 1, self.__turn)[1]
            if all(side is None for side in winSides):
                return True
            
        if y != 0 and grid[y - 1][x - 1].getState() != 0 and (grid[y - 1][x - 1].getPlayer() == 2 - self.__turn or grid[y - 1][x - 1].getPlayer() == 0):
            winSides = self.__table.checkWinNeighbors(x - 1, y - 1, self.__turn)[1]
            if all(side is None for side in winSides):
                return True
            
        if y != 6 and grid[y + 1][x + 1].getState() != 0 and (grid[y + 1][x + 1].getPlayer() == 2 - self.__turn or grid[y + 1][x + 1].getPlayer() == 0):
            winSides = self.__table.checkWinNeighbors(x + 1, y + 1, self.__turn)[1]
            if all(side is None for side in winSides):
                return True
            
        if y != 6 and grid[y + 1][x - 1].getState() != 0 and (grid[y + 1][x - 1].getPlayer() == 2 - self.__turn or grid[y + 1][x - 1].getPlayer() == 0):
            winSides = self.__table.checkWinNeighbors(x - 1, y + 1, self.__turn)[1]
            if all(side is None for side in winSides):
                return True
            
        return False

            
def createGame():
    return Game()
