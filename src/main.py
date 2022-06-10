# ICI LE MENU
import game
from tkinter import *
from PIL import ImageTk, Image


class Menus:
    w = Tk()
    w.geometry("900x500")
    w.configure(bg="#262626")
    w.resizable(0, 0)
    w.title("KAMON")

    def default_home():
        frame2 = Frame(w, width=900, height=455, bg="#262626")
        frame2.place(x=0, y=45)
        frame3 = Frame(w, width=900, height=455, bg="#262626")
        frame3.place(x=0, y=50)
        label2 = Label(
            frame2, text="Bienvenue sur le jeu KAMON", fg="white", bg="#262626"
        )
        label2.config(font=("Comic Sans MS", 50))
        label2.place(x=290, y=150 - 45)
        label3 = Label(
            frame3, text="Veuillez déroulez le menu", fg="white", bg="#262626"
        )
        label3.config(font=("Comic Sans MS", 20))
        label3.place(x=290, y=150 - 45)

    def singleplayer():
        frame1.destroy()
        frame2 = Frame(w, width=900, height=455, bg="#262626")
        frame2.place(x=0, y=45)
        label2 = Label(frame2, text="SinglePlayer", fg="white", bg="#262626")
        label2.config(font=("Comic Sans MS", 90))
        label2.place(x=290, y=150 - 45)
        toggle_win()

    def multiPlayer():
        frame1.destroy()
        frame2 = Frame(w, width=900, height=455, bg="white")
        frame2.place(x=0, y=45)
        label2 = Label(frame2, text="MultiPlayer", fg="black", bg="white")
        label2.config(font=("Comic Sans MS", 90))
        label2.place(x=290, y=150 - 45)
        toggle_win()

    def option():
        frame1.destroy()
        f2 = Frame(w, width=900, height=455, bg="white")
        f2.place(x=0, y=45)
        l2 = Label(f2, text="Option", fg="black", bg="white")
        l2.config(font=("Comic Sans MS", 90))
        l2.place(x=320, y=150 - 45)
        toggle_win()

    def toggle_win():
        global frame1
        frame1 = Frame(w, width=300, height=500, bg="#12c4c0")
        frame1.place(x=0, y=0)

        # buttons
        def bttn(x, y, text, bcolor, fcolor, cmd):
            def entrer(e):
                myButton1["background"] = bcolor  # ffcc66
                myButton1["foreground"] = "#262626"  # 000d33

            def sortir(e):
                myButton1["background"] = fcolor
                myButton1["foreground"] = "#262626"

            myButton1 = Button(
                frame1,
                text=text,
                width=42,
                height=2,
                fg="#262626",
                border=0,
                bg=fcolor,
                activeforeground="#262626",
                activebackground=bcolor,
                command=cmd,
            )

            myButton1.bind("<Enter>", entrer)
            myButton1.bind("<Leave>", sortir)

            myButton1.place(x=x, y=y)

        bttn(0, 80, "Singleplayer", "#0f9d9a", "#12c4c0", singleplayer)
        bttn(0, 117, "MultiPlayer", "#0f9d9a", "#12c4c0", multiPlayer)
        bttn(0, 154, "Option", "#0f9d9a", "#12c4c0", option)

        #
        def dele():
            frame1.destroy()
            b2 = Button(
                w,
                image=img1,
                command=toggle_win,
                border=0,
                bg="#262626",
                activebackground="#262626",
            )
            b2.place(x=5, y=8)

        global img2
        img2 = ImageTk.PhotoImage(Image.open("close.png"))

        Button(
            frame1,
            image=img2,
            border=0,
            command=dele,
            bg="#12c4c0",
            activebackground="#12c4c0",
        ).place(x=5, y=10)

    default_home()

    img1 = ImageTk.PhotoImage(Image.open("open.png"))

    global b2
    b2 = Button(
        w,
        image=img1,
        command=toggle_win,
        border=0,
        bg="#262626",
        activebackground="#262626",
    )
    b2.place(x=5, y=8)

    def singlePlayerMode(self):
        self.window.destroy()
        game.gameRun("v1")

    def multiPlayerMode(self):
        self.window.destroy()
        game.gameRun("v1")

    def menuRun():
        start = Menus()

    w.mainloop()


""" Init some frame for the contents
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





if __name__ == "__main__":
    menuRun()
"""
