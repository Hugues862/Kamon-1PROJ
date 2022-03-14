
from .hexagone import hexa
from random import *
import pandas as pd
import numpy as np


class Table():

    def __init__(self, theme="original"):

        self.__grid = self.initGrid(theme)
        self.__lastCoord = (0, 0) # Used to remove golden ring

    # Getters

    def getGridState(self):
        return [[item.getState() for item in row] for row in self.__grid]
    
    def getGridSide(self):
        return [[item.getSide() for item in row] for row in self.__grid]

    def getGrid(self):
        return self.__grid
    
    def getLastCoord(self):
        return self.__lastCoord
    
    # Methods

    def initGrid(self, theme):

        inside = [0]
        grid = []

        for i in range(7):
            tmp = []

            for j in range(abs(3 - i)):
                tmp.append(hexa(0))

            for j in range(7 - abs(3 - i)):

                test = randint(-1, 36)
                while test in inside:
                    test = randint(-1, 36)
                inside.append(test)

                # Assigning the cells on the board of the map, colors for borders

                side = None

                if i == 0:
                    if j == 0:
                        side = "G&Y"
                    elif j == 7 - abs(3 - i) - 1:
                        side = "G&B"
                    else:
                        side = "G"

                elif i == 6:
                    if j == 0:
                        side = "G&B"
                    elif j == 7 - abs(3 - i) - 1:
                        side = "G&Y"
                    else:
                        side = "G"

                elif i == 1 or i == 2:
                    if j == 0:
                        side = "Y"
                    elif j == 7 - abs(3 - i) - 1:
                        side = "B"

                elif i == 4 or i == 5:
                    if j == 0:
                        side = "B"
                    elif j == 7 - abs(3 - i) - 1:
                        side = "Y"

                elif i == 3:
                    if j == 0 or j == 7 - abs(3 - i) - 1:
                        side = "B&Y"

                tmp.append(hexa(test, theme, side))
                tmp.append(hexa(0))

            for j in range(abs(3 - i)):
                tmp.append(hexa(0))

            grid.append(tmp)

        return grid

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
        print(res)
        return res
    
    def printSide(self):
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

        tmp = self.getGridSide()
        res = pd.DataFrame(tmp).replace(to_replace=0, value="")
        print(res)
        return res
    
t = Table()
t.printGrid()

