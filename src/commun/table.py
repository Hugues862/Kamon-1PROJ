from .hexagone import hexa
from random import *
import pandas as pd


class Table:
    def __init__(self, theme):

        self.__grid = self.initGrid(theme)
        self.__selectedCoord = None  # Used to remove red ring
        self.__lastCoord = None  # Used to remove golden ring

    # Getters

    def getGridState(self):
        return [[item.getState() for item in row] for row in self.__grid]

    def getGridSide(self):
        return [[item.getSide() for item in row] for row in self.__grid]

    def getGrid(self):
        return self.__grid

    def getSelectedCoord(self):
        return self.__selectedCoord

    def getLastCoord(self):
        return self.__lastCoord

    def setSelectedCoord(self, x, y):
        self.__selectedCoord = (x, y)

    def setLastCoord(self, x, y):
        self.__lastCoord = (x, y)

    # Methods

    def initGrid(self, theme):
        """Initialization of the game grid

        Args:
            theme (int): applied theme for the game

        Returns:
            matrix: applied grid for the game
        """        

        inside = [0]
        grid = []

        for i in range(7):
            tmp = []

            for j in range(abs(3 - i)):
                tmp.append(hexa(0, theme))

            for j in range(7 - abs(3 - i)):

                rdmValue = randint(-1, 36)
                while rdmValue in inside:
                    rdmValue = randint(-1, 36)
                inside.append(rdmValue)

                # Assigning the cells on the board of the map, colors for borders

                side = None

                if i == 0:
                    if j == 0:
                        side = "B1&Y1"
                    elif j == 7 - abs(3 - i) - 1:
                        side = "B1&G1"
                    else:
                        side = "B1"

                elif i == 6:
                    if j == 0:
                        side = "B2&G2"
                    elif j == 7 - abs(3 - i) - 1:
                        side = "B2&Y2"
                    else:
                        side = "B2"

                elif i == 1 or i == 2:
                    if j == 0:
                        side = "Y1"
                    elif j == 7 - abs(3 - i) - 1:
                        side = "G1"

                elif i == 4 or i == 5:
                    if j == 0:
                        side = "G2"
                    elif j == 7 - abs(3 - i) - 1:
                        side = "Y2"

                elif i == 3:
                    if j == 0:
                        side = "G2&Y1"
                    elif j == 7 - abs(3 - i) - 1:
                        side = "G1&Y2"

                tmp.append(hexa(rdmValue, theme, side))
                tmp.append(hexa(0, theme))

            for j in range(abs(3 - i)):
                tmp.append(hexa(0, theme))

            grid.append(tmp)

        return grid

    def checkNeighbors(self, x, y, turn, neighbors, sides):

        """Function to check the boxes around the position x,y

        Returns:
            list[list[(x,y)],list[str]]: Return a list of position and a list of string (side)
        """    

        # print("tableCheck")
        # print(neighbors)
        # print(sides)

        if (x, y) in neighbors:
            return neighbors, sides

        if self.__grid[y][x].getSide() not in sides:
            sides.append(self.__grid[y][x].getSide())

        if (x, y) not in neighbors:
            neighbors.append((x, y))

        #Check if inside board the player can play and if the cells is blank
        if (
            x != abs(3 - y)
            and self.__grid[y][x - 2].getState() != 0
            and self.__grid[y][x - 2].getPlayer() == 1 + turn
        ):
            # Check the neighbors of the cells;if they are allied add it to neighbors and side
            neighbors, sides = self.checkNeighbors(x - 2, y, turn, neighbors, sides) 

        if (
            x != 12 - abs(3 - y)
            and self.__grid[y][x + 2].getState() != 0
            and self.__grid[y][x + 2].getPlayer() == 1 + turn
        ):
            neighbors, sides = self.checkNeighbors(x + 2, y, turn, neighbors, sides)

        if (
            y != 0
            and self.__grid[y - 1][x + 1].getState() != 0
            and self.__grid[y - 1][x + 1].getPlayer() == 1 + turn
        ):
            neighbors, sides = self.checkNeighbors(x + 1, y - 1, turn, neighbors, sides)

        if (
            y != 0
            and self.__grid[y - 1][x - 1].getState() != 0
            and self.__grid[y - 1][x - 1].getPlayer() == 1 + turn
        ):
            neighbors, sides = self.checkNeighbors(x - 1, y - 1, turn, neighbors, sides)

        if (
            y != 6
            and self.__grid[y + 1][x + 1].getState() != 0
            and self.__grid[y + 1][x + 1].getPlayer() == 1 + turn
        ):
            neighbors, sides = self.checkNeighbors(x + 1, y + 1, turn, neighbors, sides)

        if (
            y != 6
            and self.__grid[y + 1][x - 1].getState() != 0
            and self.__grid[y + 1][x - 1].getPlayer() == 1 + turn
        ):
            neighbors, sides = self.checkNeighbors(x - 1, y + 1, turn, neighbors, sides)

        return neighbors, sides

    def checkWinNeighbors(self, x, y, turn, neighbors, sides):

        """Function that checks the 3 win conditions

        Returns:
            list[list[(x,y)],list[str]]: Return a list of position and a list of string (side)
        """    
        if len(sides) == 0 or (
            all(side is None for side in sides) and (x, y) not in neighbors
        ):

            neighbors.append((x, y))

            if self.__grid[y][x].getSide() not in sides:
                # print(sides)
                sides.append(self.__grid[y][x].getSide())

            #Check if inside the board if the neighbors have the same state as the initial cell to verify a win condition
            if (
                x != abs(3 - y)
                and self.__grid[y][x - 2].getState() != 0
                and (
                    self.__grid[y][x - 2].getPlayer() == 2 - turn
                    or self.__grid[y][x - 2].getPlayer() == 0
                )
            ):
                # Check the  win condition of the neighbors of the cells;if they are allied add it to neighbors and side
                neighbors, sides = self.checkWinNeighbors(
                    x - 2, y, turn, neighbors, sides
                )

            if (
                x != 12 - abs(3 - y)
                and self.__grid[y][x + 2].getState() != 0
                and (
                    self.__grid[y][x + 2].getPlayer() == 2 - turn
                    or self.__grid[y][x + 2].getPlayer() == 0
                )
            ):
                neighbors, sides = self.checkWinNeighbors(
                    x + 2, y, turn, neighbors, sides
                )

            if (
                y != 0
                and self.__grid[y - 1][x + 1].getState() != 0
                and (
                    self.__grid[y - 1][x + 1].getPlayer() == 2 - turn
                    or self.__grid[y - 1][x + 1].getPlayer() == 0
                )
            ):
                neighbors, sides = self.checkWinNeighbors(
                    x + 1, y - 1, turn, neighbors, sides
                )

            if (
                y != 0
                and self.__grid[y - 1][x - 1].getState() != 0
                and (
                    self.__grid[y - 1][x - 1].getPlayer() == 2 - turn
                    or self.__grid[y - 1][x - 1].getPlayer() == 0
                )
            ):
                neighbors, sides = self.checkWinNeighbors(
                    x - 1, y - 1, turn, neighbors, sides
                )

            if (
                y != 6
                and self.__grid[y + 1][x + 1].getState() != 0
                and (
                    self.__grid[y + 1][x + 1].getPlayer() == 2 - turn
                    or self.__grid[y + 1][x + 1].getPlayer() == 0
                )
            ):
                neighbors, sides = self.checkWinNeighbors(
                    x + 1, y + 1, turn, neighbors, sides
                )

            if (
                y != 6
                and self.__grid[y + 1][x - 1].getState() != 0
                and (
                    self.__grid[y + 1][x - 1].getPlayer() == 2 - turn
                    or self.__grid[y + 1][x - 1].getPlayer() == 0
                )
            ):
                neighbors, sides = self.checkWinNeighbors(
                    x - 1, y + 1, turn, neighbors, sides
                )

        return neighbors, sides

    def printGrid(self):
        """Prints a pretty version of the grid, instead of having :
        [[0, 0, 0, -1, 0, 16, 0, 14, 0, 33, 0, 0, 0, 0], [0, 0, 21, 0, 32, 0, 23, 0, 28, 0, 30, 0, 0, 0], ...]

        we have

                0   1   2   3   4   5   6   7   8   9   10  11 12 13
        0              -1      16      14      33
        1          21      32      23      28      30
        2      13      17      31      19       3       7
        3  35      20       2      25       9      11      8
        4      27      34      22      26      18      29
        5           4       1      36       5      24
        6              15      12       6      10

        Returns:
            [pd.DataFrame]: dataframe version of self.__grid, 0 replaced with empty str
        """

        tmp = self.getGridState()
        res = pd.DataFrame(tmp).replace(to_replace=0, value="")
        return res

    def printSide(self):
        """ """

        tmp = self.getGridSide()
        res = pd.DataFrame(tmp).fillna(value="")
        return res

    def isPossible(self, x, y):
        """Checks if the position of our cursor during the click is possible to transform the box

        Args:
            x (int): position x of our cursor
            y (int): position y of our cursor

        Returns:
             list[list[(x,y)], list[list[int]: Return the last coordinates and the player index
        """        
        return (
            self.__lastCoord == None
            or self.__grid[y][x].getColor()
            == self.__grid[self.__lastCoord[1]][self.__lastCoord[0]].getColor()
            or self.__grid[y][x].getImage()
            == self.__grid[self.__lastCoord[1]][self.__lastCoord[0]].getImage()
        ) and (self.__grid[y][x].getPlayer() == 0)
