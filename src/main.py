import os
import pathlib
import dotenv
import multiprocessing

import time
from tkinter import *
from PIL import ImageTk, Image

import displayGame, server

WorkingDirectory = pathlib.Path().resolve()
BACKGROUNDCOLOR = "#262626"
MAINFONTCOLOR = "#8A2BE2"


def startMenu():
    """Main Menu Function Initializing global variables and starting the window with the Home Menu as default."""

    global theme  # ! Variable responsible for the used theme
    theme = "original"

    global w  # ! Main window variable
    w = Tk()
    w.geometry("900x500")
    w.configure(bg=BACKGROUNDCOLOR)
    w.resizable(0, 0)
    w.title("KAMON")

    global serverThread  # ! Thread responsible for running the server in onlineMode
    serverThread = multiprocessing.Process(
        target=thread_function,
        name="Server Thread",
        args=(theme,),
        kwargs={},
    )

    # * Calls the Home Menu
    default_home()

    global openImg  # ? Image variable to open the drop down menu
    openImg = ImageTk.PhotoImage(
        Image.open(str(WorkingDirectory) + "/src/assets/menu/open.png")
    )

    global closeImg  # ? Image variable to close the drop down menu
    closeImg = ImageTk.PhotoImage(
        Image.open(str(WorkingDirectory) + "/src/assets/menu/close.png")
    )

    global dropMenu  # ! Variable to use the Drop down menu
    dropMenu = Button(
        w,
        image=openImg,
        command=toggle_win,
        border=0,
        bg=MAINFONTCOLOR,
        activebackground=BACKGROUNDCOLOR,
    )
    dropMenu.place(x=5, y=8)

    w.mainloop()


# * Switch / Start Windows & Server Fuctions


def multiPlayerMode(p1, p2):
    """Will destroy the current window and launch the game loop without an AI player.

    Args:
        p1 (str): Name used for Player 1.
        p2 (str): Name used for Player 2.
    """

    # ? If any of the players did not input any name, then assign default

    if len(p1) == 0:
        p1 = "Player 1"
    if len(p2) == 0:
        p2 = "Player 2"

    w.destroy()
    displayGame.startGame("solo", p1=p1, p2=p2, theme=theme)


def singlePlayerMode():
    """Will destroy the current window and launch the game loop with an AI player."""

    w.destroy()
    displayGame.startGame("bot", theme=theme)


def onlineMode(ip=None, create=False):
    """Will destroy the current window and launch the game and connect it to a server.
    Will start server before launching the game if asked.

    Args:
        ip (str, optional): Ip address to which the game will connect to. Defaults to None.
        create (bool, optional): If True, start the server thread and launch the game connected to same server. Defaults to False.
    """

    if create:  # ! If user is asking to Start Server

        global serverThread

        # ? Kills the server if already running

        if serverThread.is_alive() == 1:
            print("Server already running")
            serverThread.terminate()
            serverThread = multiprocessing.Process(
                target=thread_function,
                name="Server Thread",
                args=(theme,),
                kwargs={},
            )

        serverThread.start()  # ? Start server

        # ? Destroy Window and start game connected to the server

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

    else:  # ! If user is asking to connect to server (IP)

        # ? Destroy Window and start game connected to the server

        w.destroy()
        displayGame.startGame("server", server_ip=ip, theme=theme)


def thread_function(theme):
    """Function used in ServerThread to run the server in a separate thread.

    Args:
        theme (str): Theme of the game.
    """

    server.runServer(theme)


# * Init functions of different menus


def default_home(first=True):
    """(Re)draws the default home menu.

    Args:
        first (bool, optional): If False, clear the canvas. Defaults to True.
    """

    global subFrame

    # ? Reset the canvas

    if not first:
        dropFrame.destroy()
        subFrame.destroy()

    # ? Draws the Menu

    subFrame = Frame(w, width=900, height=455, bg=BACKGROUNDCOLOR)
    subFrame.pack(anchor=CENTER, expand=True)

    title = Label(
        subFrame, text="BIENVENUE SUR LE JEU", fg=MAINFONTCOLOR, bg=BACKGROUNDCOLOR
    )
    title.config(font=("Big John PRO", 50))
    title.pack(side=TOP)

    subTitle = Label(subFrame, text="KAMON", fg="white", bg=BACKGROUNDCOLOR)
    subTitle.config(font=("Big John PRO", 50))
    subTitle.pack(side=TOP)

    soloButt = Button(
        subFrame,
        text="Start Against Bot",
        font=("Big John PRO", 30),
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
        command=singlePlayerMode,
    )
    soloButt.pack(side=TOP, ipadx=20, padx=30, pady=20)


def multiplayer():
    """Draws the multiplayer menu."""

    global subFrame

    # ? Reset the canvas

    dropFrame.destroy()
    subFrame.destroy()

    # ? Draws the Menu

    subFrame = Frame(w, width=900, height=455, bg=BACKGROUNDCOLOR)
    subFrame.pack(anchor=CENTER, expand=True)

    title = Label(
        subFrame,
        text="YOU CHOOSE MULTIPLAYER MODE ",
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
    )
    title.config(font=("Big John PRO", 35))
    title.pack(side=TOP)

    # ? Player Name

    # * Player One
    playerOne = LabelFrame(
        subFrame,
        text="Joueur 1",
        font=("Big John PRO", 30),
        bg=BACKGROUNDCOLOR,
        fg=MAINFONTCOLOR,
    )
    playerOne.pack(side=TOP)

    player1Name = Label(
        playerOne, text=" Nom :", fg="black", bg="yellow", font=("Big John PRO", 12)
    )
    player1Name.pack(padx=10, pady=10, side=LEFT)

    # ? Player Name Input
    player1Entry = Entry(playerOne)
    player1Entry.pack(padx=5, pady=5, side=LEFT)

    # * Player Two
    playerTwo = LabelFrame(
        subFrame,
        text="Joueur 2",
        font=("Big John PRO", 30),
        bg=BACKGROUNDCOLOR,
        fg=MAINFONTCOLOR,
    )
    playerTwo.pack(side=TOP)

    player2Name = Label(
        playerTwo, text="Nom :", fg="black", bg="yellow", font=("Big John PRO", 12)
    )
    player2Name.pack(padx=10, pady=10, side=LEFT)

    # ? Player Name Input
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
    """Draws the online menu."""

    global subFrame

    # ? Reset the canvas

    dropFrame.destroy()
    subFrame.destroy()

    # ? Draws the Menu

    subFrame = Frame(w, width=900, height=455, bg=BACKGROUNDCOLOR)
    subFrame.pack(anchor=CENTER, expand=True)

    title = Label(
        subFrame,
        text=" YOU CHOOSE THE ONLINE MODE",
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
    )
    title.config(font=("Big John PRO", 30))
    title.pack(side=TOP)

    # ? IP Address to Connect to

    ipFrame = LabelFrame(
        subFrame,
        text="CONNECT TO PLAYER",
        font=("Big John PRO", 25),
        bg=BACKGROUNDCOLOR,
        fg=MAINFONTCOLOR,
    )
    ipFrame.pack(padx=5, pady=5, side=TOP)

    ipAdrr = Label(
        ipFrame, text=" Server IP :", fg="red", bg="yellow", font=("Big John PRO", 20)
    )
    ipAdrr.pack(padx=10, pady=10, anchor=CENTER)

    # ? IP Address Input
    ipEntry = Entry(ipFrame)
    ipEntry.pack(padx=5, pady=5, anchor=CENTER)

    connButt = Button(
        subFrame,
        text="CONNECT",
        font=("Big John PRO", 15),
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
        command=lambda: onlineMode(ip=ipEntry.get()),
    )
    connButt.pack(side=TOP, ipadx=20, padx=30, pady=20)

    createButt = Button(
        subFrame,
        text="CREATE GAME",
        font=("Big John PRO", 15),
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
        command=lambda: onlineMode(create=True),
    )
    createButt.pack(side=TOP, ipadx=20, padx=30, pady=20)


def option():
    """Draws the option menu."""

    global subFrame
    global theme

    # ? Reset the canvas

    dropFrame.destroy()
    subFrame.destroy()

    # ? Draws the Menu

    subFrame = Frame(w, width=900, height=455, bg=BACKGROUNDCOLOR)
    subFrame.pack(anchor=CENTER, expand=True)

    title = Label(
        subFrame, text="CHOOSE YOUR THEME", fg=MAINFONTCOLOR, bg=BACKGROUNDCOLOR
    )
    title.config(font=("Big John PRO", 30))
    title.pack(side=TOP, pady=15)

    # ? Theme Buttons

    buttFrame = Frame(subFrame, bg=BACKGROUNDCOLOR)
    buttFrame.pack(padx=5, pady=15, side=TOP)

    buttFrame2 = Frame(subFrame, bg=BACKGROUNDCOLOR)
    buttFrame2.pack(padx=5, pady=15, side=TOP)

    originalButt = Button(
        buttFrame,
        font=("Big John PRO", 15),
        text="Original",
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
        command=lambda: change_theme(0),
    )

    carsButt = Button(
        buttFrame,
        font=("Big John PRO", 15),
        text="Cars",
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
        command=lambda: change_theme(1),
    )

    animeButt = Button(
        buttFrame,
        font=("Big John PRO", 15),
        text="Anime",
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
        command=lambda: change_theme(2),
    )

    superheroButt = Button(
        buttFrame2,
        font=("Big John PRO", 15),
        text="Super Hero",
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
        command=lambda: change_theme(3),
    )

    trollButt = Button(
        buttFrame2,
        font=("Big John PRO", 15),
        text="Surprise !",
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
        command=lambda: change_theme(4),
    )

    trueTrollButt = Button(
        buttFrame2,
        font=("Big John PRO", 15),
        text="Even more Surprise !",
        fg=MAINFONTCOLOR,
        bg=BACKGROUNDCOLOR,
        command=lambda: change_theme(5),
    )

    originalButt.pack(side=LEFT, pady=15, padx=25)
    carsButt.pack(side=LEFT, pady=15, padx=25)
    animeButt.pack(side=LEFT, pady=15, padx=25)
    superheroButt.pack(side=LEFT, pady=15, padx=25)
    trollButt.pack(side=LEFT, pady=15, padx=25)
    trueTrollButt.pack(side=LEFT, pady=15, padx=25)


def change_theme(change):
    """Change the theme to the asked theme.

    Args:
        change (int): Value assigned to different themes (0 - 5).
    """

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
    """Create or delete the drop down menu."""

    # ? Creates the Drop Down Menu and its Buttons

    global dropFrame
    dropFrame = Frame(w, width=300, height=500, bg=MAINFONTCOLOR)
    dropFrame.place(x=0, y=0)

    # * Create button function, specific to the drop down menu
    def bttn(y, text, bcolor, fcolor, cmd):

        # ? While Hover
        def on_entera(e):
            newButton["background"] = bcolor  # ffcc66
            newButton["foreground"] = BACKGROUNDCOLOR  # 000d33

        # ? While Not Hover
        def on_leavea(e):
            newButton["background"] = fcolor
            newButton["foreground"] = BACKGROUNDCOLOR

        newButton = Button(
            dropFrame,
            text=text,
            width=42,
            height=2,
            fg=BACKGROUNDCOLOR,
            border=0,
            bg=fcolor,
            activeforeground=BACKGROUNDCOLOR,
            activebackground=bcolor,
            command=cmd,
        )

        newButton.bind("<Enter>", on_entera)
        newButton.bind("<Leave>", on_leavea)

        #newButton.pack(fill = BOTH)
        newButton.place(relx=0.5, rely=y, anchor=CENTER)
    # * Handles the Close button for the drop down menu
    def dele():
        dropFrame.destroy()
        dropMenu = Button(
            w,
            image=openImg,
            command=toggle_win,
            border=0,
            bg=MAINFONTCOLOR,
            activebackground="#FFFAF0",
        )
        dropMenu.place(x=5, y=8)

    # * Drop down menu buttons define
    bttn(0.375, "H O M E", "#FFFAF0", MAINFONTCOLOR, lambda: default_home(False))
    bttn(0.45, "M U L T I P L A Y E R", "#FFFAF0", MAINFONTCOLOR, multiplayer)
    bttn(0.525, "O N L I N E", "#FFFAF0", MAINFONTCOLOR, online)
    bttn(0.6, "O P T I O N", "#FFFAF0", MAINFONTCOLOR, option)

    Button(
        dropFrame,
        image=closeImg,
        border=0,
        command=dele,
        bg=MAINFONTCOLOR,
        activebackground=MAINFONTCOLOR,
    ).place(x=5, y=10)


if __name__ == "__main__":
    startMenu()


# Ip du serveur : Non défini
# Boutton Start Serveur
#

# Ip du serveur : ""
# Boutton Se connecter au serveur
