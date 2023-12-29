import time
import random
import tkinter as tk
from game_window import GameBoard
from utils import *

class StartUp:
    
    def __init__(self):
        """Skapar en huvudloop.
        Inparametrar: self"""
        self.info = None
        self.sizeEntry = None
        self.bombSizeEntry = None

    def infowindow(self):
        """skapar info fonstret med att skriva i olika varde
       inparametar ---
       utparametrar---
       """
        self.info = tk.Tk()
        self.info.geometry("500x300")
        self.info.title("Info")

        # Create labels and entry widgets for size and bombSize
        welcomeText = tk.Label(self.info, text="Welcome to the program, use X to go inside flagging mode,\nuse X one more time to go outside flagging mode\nGood Luck!")
        welcomeText.grid(row=0, column=1, padx=10, pady=5)

        sizeLabel = tk.Label(self.info, text="Enter size (Default 8):")
        sizeLabel.grid(row=1, column=0, padx=10, pady=5)
        self.sizeEntry = tk.Entry(self.info)
        self.sizeEntry.grid(row=1, column=1, padx=10, pady=5)
        bombSizeLabel = tk.Label(self.info, text="Enter bombSize (Default 10):")
        bombSizeLabel.grid(row=2, column=0, padx=10, pady=5)
        self.bombSizeEntry = tk.Entry(self.info)
        self.bombSizeEntry.grid(row=2, column=1, padx=10, pady=5)

        startButton = tk.Button(self.info, text="Start Game", command=self.startGame)
        startButton.grid(row=3, column=0, columnspan=2, pady=10)

        self.info.mainloop()

    def startGame(self):
        """tolkar vad som har skrivits i falten(rutorna) for storlek, 
       inparametar ---
       utparametrar nytt varde på size och bombSize
       """
        try:
            size = int(self.sizeEntry.get())
        except ValueError:
            size = 8  

        try:
            bombSize = int(self.bombSizeEntry.get())
        except ValueError:
            bombSize = 10  

        self.info.destroy()  
        self.start(size,bombSize)

    

    def start(self,size,bombSize):
        """
        startar programet och upptadeterar text på rutor stannaar när går till rott destory. 
        huvudloppen 
        1. startartiden
        2. fyller spelplanen tom
        3. planterar bombs
        4. skriver ut spelplanen
        5. tar in en inmatning och tolkar
        6. kollar om förlust
        6.1 om 6. stämmer skriver ut spelplanen med bombs och avslutar programet
        7. kollar bombs i närheten
        8. skriver ut spelplanen
        9. kollar om vinst
        9.1 om 9. stämmer avslutar tid och frågar efter namn för att skriva ut resultat från filen avslutar därefter programet
        10. repetera från steg 5.
        """
        if bombSize>=0 and bombSize<=(size*size) and size>0:
            
            root = tk.Tk()
            startTime = time.time()
            grid = GameBoard(bombSize,size,root,startTime)
            #print(grid) dbg för allocera plats var den skapas
            bombs = plantBombs(bombSize,size)
            grid.mainWindow(bombs)

            root.mainloop()
        elif bombSize<0:
            print("DBG:BOMBSIZE: TO SMALL size OF BOMBS",bombSize,"Please enter between 0 and",size*size)
            infowindow()
        elif bombSize>(size*size):
            print("DBG:BOMBSIZE: TO BIG size OF BOMBS",bombSize,"Please enter between 0 and",size*size)
            self.infowindow()
        elif size<=0:
            print("DBG:size: TO SMALL size OF SpelPlan",bombSize,"Please enter number over 0 ")
            self.infowindow()
