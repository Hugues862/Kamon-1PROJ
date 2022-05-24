from tkinter import *
import v1
import main
from tkinter import font
import pathlib

WorkingDirectory = pathlib.Path().resolve()


class win():
    
    def __init__(self, winner):
        # Init the window
        self.window = Tk()
        self.window.geometry("1300x900")
        self.window.title(' WIN')
        bg = PhotoImage(
            file= str(str(WorkingDirectory) + "/src/assets/Elements for the Menu/imagewin.ppm"))
        
        image = Label(self.window, image=bg)
        image.place(x=0, y=0)

         # Init some frame for the contents
        frameRejouer = Frame(self.window)
        frameQuit = Frame(self.window)

        # Contents of the window
        # Text
        winnerText = Label(self.window, text = "Player " + str(1 + winner) + " won the game !", font=('Courrier', 60), fg='black')
        
        texte1 = Label(self.window, text="Do you want to restart the game",
                       font=('Courrier', 40), fg='black')
        
        winnerText.pack(side='top', padx = 10, pady = 10)
        texte1.pack(side='top', padx = 10, pady = 10)

        # Button
        button1 = Button(frameRejouer, text="RESTART", font=('Helvetica', 20), borderwidth=(
            20), foreground=("red"), relief='ridge', highlightthickness=(10), command = self.restart)
        button1.grid(row=0, column=0, pady=20, ipadx=30)

        button2 = Button(frameQuit, text="BACK TO THE MENU", font=('Helvetica', 20), borderwidth=(
            20), foreground=("red"), relief='ridge', highlightthickness=(10), command = self.quit)
        button2.grid(row=0, column=0, pady=20, ipadx=30)


        frameRejouer.pack()
        frameQuit.pack()
        
        self.window.mainloop()
    
    def restart(self):
        self.window.destroy()
        v1.gameRun()       

    def quit(self):
        self.window.destroy()
        main.menuRun()
        
def winRun(winner):
    end = win(winner)
    
# winRun(1)
