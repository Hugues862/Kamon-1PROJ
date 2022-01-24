
from hexagone import hexa
from random import *


class table():

    def __init__(self, theme="original"):

        self.__grid = self.initGrid(theme)

    def getGrid(self):
        return self.__grid

    def initGrid(self, theme):

        inside = []
        grid = []

        for i in range(7):
            tmp = []

            for j in range(abs(3 - i)):
                tmp.append(hexa(0))

            for j in range(7 - abs(3 - i)):

                test = randint(1, 36)
                while test in inside:
                    test = randint(1, 36)
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
print(t)
