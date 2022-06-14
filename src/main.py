import displayGame as game
from tkinter import *
from PIL import ImageTk, Image
import pathlib

WorkingDirectory = pathlib.Path().resolve()

w = Tk()
w.geometry("900x500")
w.configure(bg="#262626")
w.resizable(0, 0)
w.title("KAMON")


def default_home():
    f2 = Frame(w, width=900, height=455, bg="#262626")
    f2.place(x=0, y=45)
    l2 = Label(f2, text="BIENVENUE SUR LE JEU", fg="#8A2BE2", bg="#262626")
    l2.config(font=("Comic Sans MS", 50))
    l2.place(x=20, y=150 - 80)
    f3 = Frame(w, width=900, height=455, bg="#262626")
    f3.place(x=0, y=200)
    l3 = Label(f3, text="KAMON", fg="white", bg="#262626")
    l3.config(font=("Comic Sans MS", 50))
    l3.place(x=250, y=1)


def singleplayer():
    f1.destroy()
    f2 = Frame(w, width=900, height=455, bg="#262626")
    f2.place(x=0, y=45)
    l2 = Label(f2, text="YOU CHOOSE SINGLEPLAYER MODE ", fg="#8A2BE2", bg="#262626")
    l2.config(font=("Comic Sans MS", 35))
    l2.place(x=40, y=150 - 45)
    bouton2 = Button(w, text="CLICK TO PLAY ", font=20)
    bouton2.pack(side="right", ipadx=20, padx=30, pady=20)
    bouton2.place(x=350, y=400)

    # Player's name label

    # Player 1
    cadre1 = LabelFrame(
        w, text="Joueur 1", font=("Comic Sans MS", 30), bg="#262626", fg="#8A2BE2"
    )
    cadre1.pack(padx=5, pady=5)
    Label1 = Label(
        cadre1, text=" Pseudo :", fg="red", bg="yellow", font=("Comic Sans MS", 12)
    )
    cadre1.place(x=100, y=250)
    Label1.pack(padx=10, pady=10, side=LEFT)
    E1 = Entry(cadre1)
    E1.pack(padx=5, pady=5, side=LEFT)

    # Player 2
    cadre2 = LabelFrame(
        w, text="Joueur 2", font=("Comic Sans MS", 30), bg="#262626", fg="#8A2BE2"
    )
    cadre2.pack(padx=5, pady=5)
    Label2 = Label(
        cadre2, text="Pseudo :", fg="black", bg="yellow", font=("Comic Sans MS", 12)
    )
    cadre2.place(x=500, y=250)
    Label2.pack(padx=10, pady=10, side=LEFT)
    E2 = Entry(cadre2)
    E2.pack(padx=5, pady=5, side=LEFT)
    toggle_win()


def multiplayer():
    f1.destroy()
    f2 = Frame(w, width=900, height=455, bg="#262626")
    f2.place(x=0, y=45)
    l2 = Label(f2, text=" YOU CHOOSE THE MULTIPLAYER MODE", fg="#8A2BE2", bg="#262626")
    l2.config(font=("Comic Sans MS", 30))
    l2.place(x=10, y=150 - 45)
    toggle_win()


def option():
    f1.destroy()
    f2 = Frame(w, width=900, height=455, bg="white")
    f2.place(x=0, y=45)
    l2 = Label(f2, text="Option", fg="black", bg="white")
    l2.config(font=("Comic Sans MS", 90))
    l2.place(x=30, y=150 - 45)
    toggle_win()


def toggle_win():
    global f1
    f1 = Frame(w, width=300, height=500, bg="#8A2BE2")
    f1.place(x=0, y=0)

    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1["background"] = bcolor  # ffcc66
            myButton1["foreground"] = "#262626"  # 000d33

        def on_leavea(e):
            myButton1["background"] = fcolor
            myButton1["foreground"] = "#262626"

        myButton1 = Button(
            f1,
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

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 50, "H O M E", "#FFFAF0", "#8A2BE2", default_home)
    bttn(0, 80, "S I N G L E P L A Y E R", "#FFFAF0", "#8A2BE2", singleplayer)
    bttn(0, 117, "M U L T I P L A Y E R", "#FFFAF0", "#8A2BE2", multiplayer)
    bttn(0, 154, "O P T I O N", "#FFFAF0", "#8A2BE2", option)

    #
    def dele():
        f1.destroy()
        b2 = Button(
            w,
            image=img1,
            command=toggle_win,
            border=0,
            bg="#8A2BE2",
            activebackground="#FFFAF0",
        )
        b2.place(x=5, y=8)

    global img2
    img2 = ImageTk.PhotoImage(Image.open(str(WorkingDirectory) + "/src/assets/menu/close.png"))

    Button(
        f1, image=img2, border=0, command=dele, bg="#8A2BE2", activebackground="#8A2BE2"
    ).place(x=5, y=10)


default_home()

img1 = ImageTk.PhotoImage(Image.open(str(WorkingDirectory) + "/src/assets/menu/open.png"))

global b2
b2 = Button(
    w,
    image=img1,
    command=toggle_win,
    border=0,
    bg="#8A2BE2",
    activebackground="#262626",
)
b2.place(x=5, y=8)


w.mainloop()


def localMode():
    w.destroy()
    game.gameRun("solo")

def singlePlayerMode():
    w.destroy()
    game.gameRun("bot")

def multiPlayerMode():
    w.destroy()
    game.gameRun("server")

def menuRun():
    start = Menus()