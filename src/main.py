import displayGame, server
from tkinter import *
from PIL import ImageTk, Image
import pathlib

WorkingDirectory = pathlib.Path().resolve()


def multiPlayerMode(p1, p2):
    
    if len(p1) == 0:
        p1 = "Player 1"
    if len(p2) == 0:
        p2 = "Player 2"
        
    w.destroy()
    displayGame.gameRun("solo", p1 = p1, p2 = p2)


def singlePlayerMode():
    w.destroy()
    displayGame.gameRun("bot")


def onlineMode(ip, create = False):
    w.destroy()
    if create:
        server.runServer()
    
    displayGame.gameRun("server")


def menuRun():
    start = Menus()


def default_home(first = True):
    
    global subFrame
    
    if not first:
        dropFrame.destroy()
        subFrame.destroy()
        
    subFrame = Frame(w, width=900, height=455, bg="#262626")
    subFrame.pack(side=TOP)
    
    title = Label(subFrame, text="BIENVENUE SUR LE JEU", fg="#8A2BE2", bg="#262626")
    title.config(font=("Comic Sans MS", 50))
    title.pack(side=TOP)
    
    subTitle = Label(subFrame, text="KAMON", fg="white", bg="#262626")
    subTitle.config(font=("Comic Sans MS", 50))
    subTitle.pack(side=TOP)
    
    soloButt = Button(
        subFrame, text="Start Against Bot", font=30, fg="#8A2BE2", bg="#262626", command=singlePlayerMode
    )
    soloButt.pack(side=TOP, ipadx=20, padx=30, pady=20)
    

def multiplayer():
    
    global subFrame
        
    dropFrame.destroy()
    subFrame.destroy()
    
    subFrame = Frame(w, width=900, height=455, bg="#262626")
    subFrame.pack(side=TOP)
    
    title = Label(subFrame, text="YOU CHOOSE MULTIPLAYER MODE ", fg="#8A2BE2", bg="#262626")
    title.config(font=("Comic Sans MS", 35))
    title.pack(side=TOP)
    
    # Player's name label

    # Player 1
    
    playerOne = LabelFrame(
        subFrame, text="Joueur 1", font=("Comic Sans MS", 30), bg="#262626", fg="#8A2BE2"
    )
    playerOne.pack(side=TOP)
    
    player1Name = Label(
        playerOne, text=" Nom :", fg="black", bg="yellow", font=("Comic Sans MS", 12)
    )
    player1Name.pack(padx=10, pady=10, side=LEFT)
    
    player1Entry = Entry(playerOne)
    player1Entry.pack(padx=5, pady=5, side=LEFT)

    # Player 2
    playerTwo = LabelFrame(
        subFrame, text="Joueur 2", font=("Comic Sans MS", 30), bg="#262626", fg="#8A2BE2"
    )
    playerTwo.pack(side=TOP)
    
    player2Name = Label(
        playerTwo, text="Nom :", fg="black", bg="yellow", font=("Comic Sans MS", 12)
    )
    player2Name.pack(padx=10, pady=10, side=LEFT)
    
    player2Entry = Entry(playerTwo)
    player2Entry.pack(padx=5, pady=5, side=LEFT)
    
    multiButt = Button(subFrame, text="Start Game", font=20, command= lambda: multiPlayerMode(p1 = player1Entry.get(), p2 = player2Entry.get()))
    multiButt.pack(side=TOP, ipadx=20, padx=30, pady=20)
    
    
def online():
    
    global subFrame
        
    dropFrame.destroy()
    subFrame.destroy()
        
    subFrame = Frame(w, width=900, height=455, bg="#262626")
    subFrame.pack(side=TOP)
    
    title = Label(subFrame, text=" YOU CHOOSE THE ONLINE MODE", fg="#8A2BE2", bg="#262626")
    title.config(font=("Comic Sans MS", 30))
    title.pack(side=TOP)
    
    
    ipFrame = LabelFrame(
        subFrame, text="CONNECT TO PLAYER", font=("Comic Sans MS", 30), bg="#262626", fg="#8A2BE2"
    )
    ipFrame.pack(padx=5, pady=5, side=TOP)
    
    ipAdrr = Label(
        ipFrame, text=" Server IP :", fg="red", bg="yellow", font=("Comic Sans MS", 12)
    )
    ipAdrr.pack(padx=10, pady=10, side=LEFT)
    
    ipEntry = Entry(ipFrame)
    ipEntry.pack(padx=5, pady=5, side=LEFT)
    

    connButt = Button(
        subFrame,
        text="CONNECT",
        font=30,
        fg="#8A2BE2",
        bg="#262626",
        command= lambda: onlineMode(ip = ipEntry.get()),
    )
    
    connButt.pack(side=TOP, ipadx=20, padx=30, pady=20)
    # connButt.place(x=350, y=400)
    
    createButt = Button(
        subFrame,
        text="CREATE GAME",
        font=30,
        fg="#8A2BE2",
        bg="#262626",
        command= lambda: onlineMode(create = True),
    )
    
    createButt.pack(side=TOP, ipadx=20, padx=30, pady=20)
    
def option():
    
    global subFrame
        
    dropFrame.destroy()
    subFrame.destroy()
    
    subFrame = Frame(w, width=900, height=455, bg="white")
    subFrame.pack(side=TOP)
    
    title = Label(subFrame, text="Option", fg="black", bg="white")
    title.config(font=("Comic Sans MS", 90))
    title.pack(side=TOP)


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
        dropFrame, image=closeImg, border=0, command=dele, bg="#8A2BE2", activebackground="#8A2BE2"
    ).place(x=5, y=10)


def start():
    global w
    w = Tk()
    w.geometry("900x500")
    w.configure(bg="#262626")
    w.resizable(0, 0)
    w.title("KAMON")
    
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
    start()


# Ip du serveur : Non défini
# Boutton Start Serveur
#

# Ip du serveur : ""
# Boutton Se connecter au serveur
