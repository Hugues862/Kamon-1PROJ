class hexa:
    def __init__(self, set, theme="original", side=None):

        self.__state = set
        self.changeColor()
        self.__side = side
        # self.__border = "None"
        self.setImage(theme)

        self.__last = False # Used to put Golden ring
        self.__player = 0

    def getState(self):
        """
        Gets the state of the Hex cell.

            Returns:
                int: Value of the state.
        """
        return self.__state

    def getColor(self):
        """
        Gets the color of the cell.

            Returns:
                str: String of the Hex color of the cell.
        """
        return self.__color

    # def getBorder(self):
    #     """
    #     Gets the color of the cell's border.

    #         Returns:
    #             str: String of the Hex color of the cell's border.
    #     """
    #     return self.__border
    
    def getSide(self):
        """
        Gets the color of the cell's side (Hex border).

            Returns:
                str: String of the Hex color of the cell's side.
        """
        return self.__side

    def getImage(self):
        """
        Gets the path of the image of this cell.

            Returns:
                str: String of a path to the asset.
        """
        return self.__src

    def getPlayer(self):
        return self.__player
    
    def getLast(self):
        return self.__last

    def changeColor(self):

        tmp = self.__state

        if tmp == 0:
            self.__color = "white"

        elif tmp == -1:
            self.__color = "black"

        elif tmp > 0 and tmp <= 6:
            self.__color = "#d97c11"

        elif tmp > 6 and tmp <= 12:
            self.__color = "#ed6b07"

        elif tmp > 12 and tmp <= 18:
            self.__color = "#117cd9"

        elif tmp > 18 and tmp <= 24:
            self.__color = "yellow"

        elif tmp > 24 and tmp <= 30:
            self.__color = "green"

        elif tmp > 30 and tmp <= 36:
            self.__color = "#b84d98"

    def setImage(self, theme: str):

        tmp = self.__state

        if tmp == 0 or tmp == -1:
            return

        if tmp - 1 % 6 == 0:

            self.__src = "../assets/" + theme + "/0.png"

        if tmp - 1 % 6 == 1:

            self.__src = "../assets/" + theme + "/1.png"

        if tmp - 1 % 6 == 2:

            self.__src = "../assets/" + theme + "/2.png"

        if tmp - 1 % 6 == 3:

            self.__src = "../assets/" + theme + "/3.png"

        if tmp - 1 % 6 == 4:

            self.__src = "../assets/" + theme + "/4.png"

        if tmp - 1 % 6 == 5:

            self.__src = "../assets/" + theme + "/5.png"

    # def changeBorder(self): # Not needed ?

    #     if self.__last:
    #         self.__border = "Red"

    #     elif self.__player == 1:
    #         self.__border = "Blue"

    #     elif self.__player == 2:
    #         self.__border = "Green"
