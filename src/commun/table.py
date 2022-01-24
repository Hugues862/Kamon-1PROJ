
from hexagone import hexa
from random import *
import pandas as pd
import numpy as np


class table():

    def __init__(self, theme="original"):

        self.__grid = self.initGrid(theme)

    def getGrid(self):
        return [[item.getState() for item in row] for row in self.__grid]

    def printGrid(self):
        tmp = self.getGrid()
        res = pd.DataFrame(tmp).replace(to_replace=0, value="")
        print(res)
        return res

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
                    if j == 7 - abs(3 - i) - 1:
                        side = "G&B"
                    else:
                        side = "G"

                elif i == 6:
                    if j == 0:
                        side = "G&B"
                    if j == 7 - abs(3 - i) - 1:
                        side = "G&Y"
                    else:
                        side = "G"

                elif i == 1 or i == 2:
                    if j == 0:
                        side = "Y"
                    if j == 7 - abs(3 - i) - 1:
                        side = "B"

                elif i == 4 or i == 5:
                    if j == 0:
                        side = "B"
                    if j == 7 - abs(3 - i) - 1:
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


t = table()
t.printGrid()
