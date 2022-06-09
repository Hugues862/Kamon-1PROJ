# ICI LE MENU
import game

from tkinter import *
from tkinter import font

# import winsound
import pathlib

WorkingDirectory = pathlib.Path().resolve()


class Menus:
    def __init__(self):
        # Init the window
        self.window = Tk()
        self.window.geometry("1300x900")
        self.window.title(" Kamon")
        bg = PhotoImage(
            file=str(
                str(WorkingDirectory) + "/src/assets/Elements for the Menu/R-_1_.ppm"
            )
        )
        my_label = Label(self.window, image=bg)
        my_label.place(x=0, y=0)

        # Init some frame for the contents
        frame1 = Frame(self.window)
        frame2 = Frame(self.window)
        frame3 = Frame(self.window)
        frame4 = Frame(self.window)

        # Contents of the window
        # Text
        texte1 = Label(
            self.window,
            text="Bienvenue sur le jeu Kamon",
            font=("Courrier", 70),
            fg="black",
        )
        texte1.pack(side="top")
        # Button
        button1 = Button(
            frame1,
            text="SinglePlayer",
            font=("Helvetica", 20),
            borderwidth=(20),
            foreground=("red"),
            relief="ridge",
            highlightthickness=(10),
            command=self.singlePlayer,
        )
        button1.grid(row=0, column=0, pady=20, ipadx=30)

        button2 = Button(
            frame2,
            text="MultiPlayer",
            font=("Helvetica", 20),
            borderwidth=(20),
            foreground=("red"),
            relief="ridge",
            highlightthickness=(10),
            command=self.multiPlayer,
        )
        button2.grid(row=0, column=0, pady=20, ipadx=30)

        button3 = Button(
            frame3,
            text="Option",
            font=("Helvetica", 20),
            borderwidth=(20),
            foreground=("red"),
            relief="ridge",
            highlightthickness=(10),
        )
        button3.grid(row=0, column=0, padx=5, pady=5, ipadx=30)

        button4 = Button(
            frame3,
            text="Edition",
            font=("Helvetica", 20),
            borderwidth=(20),
            foreground=("red"),
            relief="ridge",
            highlightthickness=(10),
        )
        button4.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

        # Player's name label

        # Player 1
        cadre1 = LabelFrame(frame4, text="Joueur 1", font=("Helvetica", 15))
        cadre1.pack(padx=5, pady=5)
        Label1 = Label(
            cadre1, text=" Pseudo :", fg="black", bg="yellow", font=("Helvetica", 12)
        )
        Label1.pack(padx=5, pady=5, side=LEFT)
        E1 = Entry(cadre1)
        E1.pack(padx=5, pady=5, side=LEFT)

        # Player 2
        cadre2 = LabelFrame(frame4, text="Joueur 2", font=("Helvetica", 15))
        cadre2.pack(padx=5, pady=5)
        Label2 = Label(
            cadre2, text="Pseudo :", fg="black", bg="yellow", font=("Helvetica", 12)
        )
        Label2.pack(padx=5, pady=5, side=LEFT)
        E2 = Entry(cadre2)
        E2.pack(padx=5, pady=5, side=LEFT)

        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame4.pack()
        self.window.mainloop()

    def singlePlayer(self):
        self.window.destroy()
        game.gameRun("v1")

    def multiPlayer(self):
        self.window.destroy()
        game.gameRun("v1")


def menuRun():
    start = Menus()


if __name__ == "__main__":
    menuRun()
