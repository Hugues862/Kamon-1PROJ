from tkinter import *
from tkinter import font

import main
import displayGame


def startWin(name):
    
    global w
    
    w = Tk()
    w.geometry("1300x900")
    w.title(" WIN")

    # Contents of the window
    # Text
    
    mainFrame = Frame(w)
    mainFrame.place(x= 0, y = 0)
    
    winnerText = Label(
        mainFrame,
        text= name + " won the displayGame !",
        font=("Big John PRO", 60),
        fg="black",
    )
    
    winnerText.pack(side=TOP)

    # Button
    returnButt = Button(
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
    
    w.destroy()
    main.startMenu()


if __name__ == "__main__":
    startWin("GIGA CHAD")
