import multiprocessing
import os
from re import T
import subprocess
import time

from pygame_menu import Theme
import displayGame, server
from tkinter import *
from PIL import ImageTk, Image
import pathlib
import dotenv

WorkingDirectory = pathlib.Path().resolve()


def multiPlayerMode(p1, p2):

    if len(p1) == 0:
        p1 = "Player 1"
    if len(p2) == 0:
        p2 = "Player 2"

    w.destroy()
    displayGame.startGame("solo", p1=p1, p2=p2, theme=theme)


def singlePlayerMode():
    w.destroy()
    displayGame.startGame("bot", theme=theme)


def thread_function(theme):

    server.runServer(theme)


def onlineMode(ip=None, create=False):

    if create:

        global serverThread
        if serverThread.is_alive() == 1:
            print("Server already running")
            serverThread.terminate()
            serverThread = multiprocessing.Process(
                target=thread_function,
                name="Server Thread",
                args=(theme,),
                kwargs={},
            )

        serverThread.start()

        # ipEntry.delete(0, END)

        # ipEntry.insert(0, serverip)

        w.destroy()
        while True:
            time.sleep(1)
            try:
                dotenv_file = dotenv.find_dotenv()
                dotenv.load_dotenv(dotenv_file)

                serverip = os.getenv("SERVER_IP")
                displayGame.startGame("server", server_ip=serverip, theme=theme)
            except:
                pass
            finally:
                break

    else:
        # TODO PASS IP ADDR
        ip = ipEntry.get()
        print(ip)
        w.destroy()
        displayGame.startGame("server", server_ip=ip, theme=theme)


def default_home(first=True):

    global subFrame

    if not first:
        dropFrame.destroy()
        subFrame.destroy()

    subFrame = Frame(w, width=900, height=455, bg="#262626")
    subFrame.pack(anchor=CENTER, expand=True)

    title = Label(subFrame, text="BIENVENUE SUR LE JEU", fg="#8A2BE2", bg="#262626")
    title.config(font=("Big John PRO", 50))
    title.pack(side=TOP)

    subTitle = Label(subFrame, text="KAMON", fg="white", bg="#262626")
    subTitle.config(font=("Big John PRO", 50))
    subTitle.pack(side=TOP)

    soloButt = Button(
        subFrame,
        text="Start Against Bot",
        font=("Big John PRO", 30),
        fg="#8A2BE2",
        bg="#262626",
        command=singlePlayerMode,
    )
    soloButt.pack(side=TOP, ipadx=20, padx=30, pady=20)


def multiplayer():

    global subFrame

    dropFrame.destroy()
    subFrame.destroy()

    subFrame = Frame(w, width=900, height=455, bg="#262626")
    subFrame.pack(anchor=CENTER, expand=True)

    title = Label(
        subFrame, text="YOU CHOOSE MULTIPLAYER MODE ", fg="#8A2BE2", bg="#262626"
    )
    title.config(font=("Big John PRO", 35))
    title.pack(side=TOP)

    # Player's name label

    # Player 1

    playerOne = LabelFrame(
        subFrame,
        text="Joueur 1",
        font=("Big John PRO", 30),
        bg="#262626",
        fg="#8A2BE2",
    )
    playerOne.pack(side=TOP)

    player1Name = Label(
        playerOne, text=" Nom :", fg="black", bg="yellow", font=("Big John PRO", 12)
    )
    player1Name.pack(padx=10, pady=10, side=LEFT)

    player1Entry = Entry(playerOne)
    player1Entry.pack(padx=5, pady=5, side=LEFT)

    # Player 2
    playerTwo = LabelFrame(
        subFrame,
        text="Joueur 2",
        font=("Big John PRO", 30),
        bg="#262626",
        fg="#8A2BE2",
    )
    playerTwo.pack(side=TOP)

    player2Name = Label(
        playerTwo, text="Nom :", fg="black", bg="yellow", font=("Big John PRO", 12)
    )
    player2Name.pack(padx=10, pady=10, side=LEFT)

    player2Entry = Entry(playerTwo)
    player2Entry.pack(padx=5, pady=5, side=LEFT)

    multiButt = Button(
        subFrame,
        text="Start Game",
        font=("Big John PRO", 20),
        command=lambda: multiPlayerMode(p1=player1Entry.get(), p2=player2Entry.get()),
    )
    multiButt.pack(side=TOP, ipadx=20, padx=30, pady=20)


def online():

    global subFrame

    dropFrame.destroy()
    subFrame.destroy()

    subFrame = Frame(w, width=900, height=455, bg="#262626")
    subFrame.pack(anchor=CENTER, expand=True)

    title = Label(
        subFrame, text=" YOU CHOOSE THE ONLINE MODE", fg="#8A2BE2", bg="#262626"
    )
    title.config(font=("Big John PRO", 30))
    title.pack(side=TOP)

    ipFrame = LabelFrame(
        subFrame,
        text="CONNECT TO PLAYER",
        font=("Big John PRO", 30),
        bg="#262626",
        fg="#8A2BE2",
    )
    ipFrame.pack(padx=5, pady=5, side=TOP)

    ipAdrr = Label(
        ipFrame, text=" Server IP :", fg="red", bg="yellow", font=("Big John PRO", 12)
    )
    ipAdrr.pack(padx=10, pady=10, side=LEFT)

    global ipEntry

    ipEntry = Entry(ipFrame)
    ipEntry.pack(padx=5, pady=5, side=LEFT)

    connButt = Button(
        subFrame,
        text="CONNECT",
        font=("Big John PRO", 30),
        fg="#8A2BE2",
        bg="#262626",
        command=lambda: onlineMode(ip=ipEntry.get()),
    )

    connButt.pack(side=TOP, ipadx=20, padx=30, pady=20)
    # connButt.place(x=350, y=400)

    createButt = Button(
        subFrame,
        text="CREATE GAME",
        font=("Big John PRO", 30),
        fg="#8A2BE2",
        bg="#262626",
        command=lambda: onlineMode(create=True),
    )

    createButt.pack(side=TOP, ipadx=20, padx=30, pady=20)


def option():

    global subFrame
    global theme

    dropFrame.destroy()
    subFrame.destroy()

    subFrame = Frame(w, width=900, height=455, bg="#262626")
    subFrame.pack(anchor=CENTER, expand=True)

    # buttons
    
    title = Label(
        subFrame, text="CHOOSE YOUR THEME", fg="#8A2BE2", bg="#262626"
    )
    title.config(font=("Big John PRO", 30))
    title.pack(side=TOP, pady=15)
    
    buttFrame = Frame(subFrame, bg="#262626")
    buttFrame.pack(padx=5, pady=15, side=TOP)
    
    buttFrame2 = Frame(subFrame, bg="#262626")
    buttFrame2.pack(padx=5, pady=15, side=TOP)
    
    originalButt = Button(
        buttFrame,
        font=("Big John PRO", 15),
        text = "Original",
        fg = "#8A2BE2",
        bg = "#262626",
        command = lambda: change_theme(0)
    )

    carsButt = Button(
        buttFrame,
        font=("Big John PRO", 15),
        text = "Cars",
        fg = "#8A2BE2",
        bg = "#262626",
        command = lambda: change_theme(1)
    )

    animeButt = Button(
        buttFrame,
        font=("Big John PRO", 15),
        text = "Anime",
        fg = "#8A2BE2",
        bg = "#262626",
        command = lambda: change_theme(2)
    )
    
    superheroButt = Button(
        buttFrame2, 
        font=("Big John PRO", 15),
        text = "Super Hero",
        fg = "#8A2BE2",
        bg = "#262626",
        command = lambda: change_theme(3)
    )

    trollButt = Button(
        buttFrame2,
        font=("Big John PRO", 15),
        text = "Surprise !",
        fg = "#8A2BE2",
        bg = "#262626",
        command = lambda: change_theme(4)
    )
    
    trueTrollButt = Button(
        buttFrame2,
        font=("Big John PRO", 15),
        text = "Even more Surprise !",
        fg = "#8A2BE2",
        bg = "#262626",
        command = lambda: change_theme(5)
    )
    
    originalButt.pack(side=LEFT, pady=15, padx=25)
    carsButt.pack(side=LEFT,pady=15, padx=25)
    animeButt.pack(side=LEFT,pady=15, padx=25)
    superheroButt.pack(side=LEFT,pady=15, padx=25)
    trollButt.pack(side=LEFT,pady=15, padx=25)
    trueTrollButt.pack(side=LEFT,pady=15, padx=25)

def change_theme(change):
    
    global theme
    
    if change == 0:
        theme = "original"
        
    elif change == 1:
        theme = "cars"
        
    elif change == 2:
        theme = "anime"
        
    elif change == 3:
        theme = "heros"
        
    elif change == 4:
        theme = "surprise"
        
    elif change == 5:
        theme = "surprise++"


def toggle_win():

    global dropFrame
    dropFrame = Frame(w, width=300, height=500, bg="#8A2BE2")
    dropFrame.place(x=0, y=0)

    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            newButton["background"] = bcolor  # ffcc66
            newButton["foreground"] = "#262626"  # 000d33

        def on_leavea(e):
            newButton["background"] = fcolor
            newButton["foreground"] = "#262626"

        newButton = Button(
            dropFrame,
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

        newButton.bind("<Enter>", on_entera)
        newButton.bind("<Leave>", on_leavea)

        newButton.place(x=x, y=y)

    bttn(0, 50, "H O M E", "#FFFAF0", "#8A2BE2", lambda: default_home(False))
    bttn(0, 80, "M U L T I P L A Y E R", "#FFFAF0", "#8A2BE2", multiplayer)
    bttn(0, 117, "O N L I N E", "#FFFAF0", "#8A2BE2", online)
    bttn(0, 154, "O P T I O N", "#FFFAF0", "#8A2BE2", option)

    #
    def dele():
        dropFrame.destroy()
        dropMenu = Button(
            w,
            image=openImg,
            command=toggle_win,
            border=0,
            bg="#8A2BE2",
            activebackground="#FFFAF0",
        )
        dropMenu.place(x=5, y=8)

    global closeImg
    closeImg = ImageTk.PhotoImage(
        Image.open(str(WorkingDirectory) + "/src/assets/menu/close.png")
    )

    Button(
        dropFrame,
        image=closeImg,
        border=0,
        command=dele,
        bg="#8A2BE2",
        activebackground="#8A2BE2",
    ).place(x=5, y=10)


def startMenu():

    global theme
    theme = "original"

    global w
    w = Tk()
    w.geometry("900x500")
    w.configure(bg="#262626")
    w.resizable(0, 0)
    w.title("KAMON")

    global serverThread
    serverThread = multiprocessing.Process(
        target=thread_function,
        name="Server Thread",
        args=(theme,),
        kwargs={},
    )

    default_home()

    global openImg
    openImg = ImageTk.PhotoImage(
        Image.open(str(WorkingDirectory) + "/src/assets/menu/open.png")
    )

    global dropMenu
    dropMenu = Button(
        w,
        image=openImg,
        command=toggle_win,
        border=0,
        bg="#8A2BE2",
        activebackground="#262626",
    )
    dropMenu.place(x=5, y=8)

    w.mainloop()


if __name__ == "__main__":
    startMenu()


# Ip du serveur : Non défini
# Boutton Start Serveur
#

# Ip du serveur : ""
# Boutton Se connecter au serveur
