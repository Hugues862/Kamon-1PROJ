from tkinter import *
from tkinter import font

import main
import displayGame


def startWin(name):
    """ Initialization of the win window with the name of the winning player

    Args:
        name (string): current player's name
    """    
    global w
    
    w = Tk()
    w.geometry("1300x900")
    w.title(" WIN")

    # Contents of the window
    # Text
    
    mainFrame = Frame(w)
    mainFrame.pack(anchor=CENTER, expand=True)
     
    winnerText = Label(  # Creation of the label (Player name + text)
        mainFrame,
        text= name + " won the Game !",
        font=("Big John PRO", 60),
        fg="black",
    )
    
    winnerText.pack(side=TOP)

    # Button
    returnButt = Button( # Creation of the ""back to menus""" button
        mainFrame,
        text="Return To Menu",
        font=("Big John PRO", 20),
        borderwidth=(20),
        foreground=("red"),
        relief="ridge",
        highlightthickness=(10),
        command= returnToMenu,
    )
    returnButt.pack(side=TOP)

    w.mainloop()

def returnToMenu():
    """Return to menu Function
    """    
    
    w.destroy()
    main.startMenu()


if __name__ == "__main__":
    startWin("GIGA CHAD")
