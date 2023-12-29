import random
import time
import os
import tkinter as tk 
from utils import*
from tkinter import PhotoImage 
from filefunctions import higscoreFile,saveFile


FILL = ' '
FLAG='F'
BOMB='B'

current_directory = os.getcwd()
BOMBIMAGEPATH = os.path.join(current_directory, "images\\bomb.png")
FLAGIMAGEPATH = os.path.join(current_directory, "images\\orangeFlag.png")
WHITEIMAGEPATH=os.path.join(current_directory, "images\\reset.png")

#----------CLASSES-----------------#
class GameBoard:
    def __init__(self,bombSize,size,root,startTime):
        """Skapar en ny insats avv SpelPlan samt satter modet till falskt
        Inparametrar: self, innehall str"""
        self.board = [[FILL for _ in range(size)] for _ in range(size)]
        self.flagMode = False
        self.flagLabel=None
        self.bombSize=bombSize
        self.size=size
        self.root=root
        self.startTime=startTime
        self.countOfFlags=0

        self.bombImage = PhotoImage(file=BOMBIMAGEPATH).subsample(70, 70) 
        self.flagImage = PhotoImage(file=FLAGIMAGEPATH).subsample(70,70)
        self.white=PhotoImage(file=WHITEIMAGEPATH).subsample(70,70)

        self.btn = [[None for _ in range(size)] for _ in range(size)]

    def changeState(self):
        """Bytter mode
       inparametar self
       returnerar bolean not mode alltså byte av mode"""
        self.flagMode = not self.flagMode

    def interpret(self, event):
        """
        Tolkar tangent inmatning fran tangentbordet
        inparametar self
        returnerar bolean not mode alltså byte av mode"""
        if event.char.upper() == 'X':
            self.changeState()

    def checkWin(self,bombs):
        """
        Tolkar tangent inmatning fran tangentbordet, kollar igenom om allt är fyllt 
        och om flagorna är inte mer än bomberna 
        inparametar self
        returnerar bolean not mode alltså byte av mode
        """
        totalFlags = 0
        stateWin=-1
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == FILL:
                    if checkBomb(bombs,(row,col))==True:
                        if stateWin==0:
                            return False
                        stateWin=1
                    else:
                        if stateWin==1:
                           return False
                        stateWin=0
                elif self.board[row][col] == FLAG:
                    totalFlags += 1
        if (totalFlags) <=self.bombSize:
            return True
        else:
            return False

    def printoutGameOver(self, bombs):
        """
        skriver ut forlorad SpelPlan
        inparametar self och bombs
        utParametrar: Skriver ut allt i tkinter
        """
        for row in range(self.size):
            for col in range(self.size):
                if checkBomb(bombs, (row, col))==False:
                    self.board[row][col] = BOMB
                    clicked_button = self.btn[row][col]
                    clicked_button.config(image=self.bombImage, compound=tk.CENTER)
        self.refreshWindow() 
       
    def flag(self, row, col):
        """skirver om en SpelPlan till F och flagar
        inparametarar self row col
        """
        self.board[row][col] = FLAG
        clicked_button = self.btn[row][col]
        clicked_button.config(image=self.flagImage, compound=tk.CENTER)
  
  
        self.countOfFlags+=1
        self.flagLabel.config(text="Bombs " + str(self.bombSize) + "\nFlags " + str(self.countOfFlags))

    def reflag(self, row, col):
        """tar bort flagningen
        inparametarar self row col
        """
        self.board[row][col] = FILL
        clicked_button = self.btn[row][col]

        # Debug print

        clicked_button.config(image=self.white, compound=tk.CENTER)
       

        self.countOfFlags -= 1
        self.flagLabel.config(text="Bombs " + str(self.bombSize) + "\nFlags " + str(self.countOfFlags))
    def mainWindow(self, bombs):
        """mainWindow i tkinter-spelplanen
        inparametarar self och bombplatsen
        returnerar ett nytt fonster
        """
        print(self.countOfFlags)
        colCounter = 'A'
        sizeOfWindow=str(100*self.size)
        self.root.geometry(f"{sizeOfWindow}x{sizeOfWindow}")

        self.root.title("Mineswepper")
        buttonFrame = tk.Frame(self.root)
        rowFrame = tk.Frame(self.root)
        
        padding = max(int(100 / (self.size * 2)),39 )
        #---------------------------skiver ut Övre raden A B (...)------#
        for _ in range(self.size):
            colLabel = tk.Label(rowFrame, text=colCounter, font=("Arial", 18))
            colLabel.pack(side=tk.LEFT, padx=padding, pady=5)
            colCounter = chr(ord(colCounter) + 1)


        rowFrame.pack() 
        #---------------------------skiver ut kanpparna [0][0](...)------#
        for i in range(self.size):
            rowFrame = tk.Frame(buttonFrame)
            rowLabel = tk.Label(rowFrame, text=str(i + 1), font=("Arial", 18))
            rowLabel.pack(side=tk.LEFT)

            buttonFrame.columnconfigure(i, weight=1)
            for j in range(self.size):
                self.btn[i][j] = tk.Button(
                    buttonFrame, text=self.board[i][j], font=("Arial", 18),
                    command=lambda row=i, column=j: self.userInput(row, column, bombs)
                )
                self.btn[i][j].grid(row=i, column=j, sticky=tk.W + tk.E)
                self.btn[i][j].config(image=self.white, compound=tk.CENTER)
        buttonFrame.pack(fill='x')

        flagFrame = tk.Frame(self.root)
        self.flagLabel = tk.Label(flagFrame, text="Bombs "+str(self.bombSize)+"\nFlags "+str(self.countOfFlags), font=("Arial", 18))
        
        self.flagLabel.pack(side=tk.LEFT)
        flagFrame.pack(side=tk.BOTTOM, anchor=tk.SE)    
        
                
        self.root.bind('<Key>', self.interpret)

    def userInput(self, row, col, bombs):
        """funktionen vidknapptryckvad som hander med resp. knapp
        inparametarar row,col(på knapp tryckningen) och bombs för jämörelse
        returnerar nytt varde for row col knappen eller loop avbrott
        """
        if self.flagMode:
            if self.board[row][col] == FILL:
                self.flag(row, col)
                if self.checkWin(bombs):
                        #print("DBG:You won!")
                        self.printoutWin()
            else:
                self.reflag(row, col)
            self.refreshWindow()
        else:
            if self.board[row][col] == FILL:
                dig = (row, col)
                if checkBomb(bombs, dig)==False:
                    
                    clicked_button = self.btn[row][col]
                    clicked_button.config(image=self.bombImage, compound=tk.CENTER)
                    #print("DBG:you lost")
                    self.printoutGameOver(bombs)
                    self.root.update_idletasks()
                    self.root.update()
                    self.loseWindow()
                    #self.root.after(2000, root.destroy)
                else:
                    self.board[row][col] = self.bombsAround(dig, bombs)
                    self.refreshWindow()
                    self.root.update_idletasks()
                    self.root.update()
                    if self.checkWin(bombs):
                        #print("DBG:Grattis! Du vann!")
                        self.printoutWin()

    def printoutWin(self):
        """Skriver ut rutan för att skriva in namn 
        inparametarar: 
        returnerar en fönster till dator
        """
        winRoot = tk.Toplevel(self.root)
        winRoot.title("You Won!")
        winLabel = tk.Label(winRoot, text="congratulations! You won!", font=("Arial", 18))
        winLabel.pack(pady=10)

        nameLabel = tk.Label(winRoot, text="Enter your name:")
        nameLabel.pack(pady=10)

        nameEntry = tk.Entry(winRoot)
        nameEntry.pack(pady=10)

        submitButton = tk.Button(winRoot, text="Send", command=lambda: self.openHighscoreWin(nameEntry.get(), winRoot))
        submitButton.pack(pady=10)

    def loseWindow(self):
        """Skriver ut rutan med text 
        inparametarar: 
        returnerar avslutning
        """
        loseRoot = tk.Toplevel(self.root)
        loseRoot.title("You lost!")
        loseLabel = tk.Label(loseRoot, text="You lost!", font=("Arial", 18))
        loseLabel.pack(pady=10)

        submitButton = tk.Button(loseRoot, text="Exit", command=lambda: self.root.destroy())
        submitButton.pack(pady=10)

    def openHighscoreWin(self, namn, winRoot):
        """öppnar filoch jämför värdet i tid sedan sckas listan vidare för att skrivas ut
        inparametarar namnet som har angivits, och nya fonstret 
        returnerar
        """
        endTime = time.time()
        passerade_seconds = int(endTime - self.startTime)
        minutes = passerade_seconds // 60
        seconds = passerade_seconds % 60
        bestResults = []
        higscoreFile(bestResults)
    
        for i in range(min(10, len(bestResults))):
            if bestResults[i][1] > minutes or (bestResults[i][1] == minutes and bestResults[i][2] > seconds):
                bestResults.insert(i, (namn, minutes, seconds))
                bestResults.pop()
                break
        
        self.showHighWin(bestResults, winRoot)
        saveFile(bestResults)

    def showHighWin(self, bestResults, winRoot):
        """Öppnar topplistan 
        inparametarar listan med toppvärden och rooten på fönster
        returnerar nedstägning av fönster
        """
        highscoreRoot = tk.Toplevel(winRoot)
        highscoreRoot.title("High Scores")

        highscoreLabel = tk.Label(highscoreRoot, text="High Scores", font=("Arial", 18))
        highscoreLabel.pack(pady=10)

        for i, resultat in enumerate(bestResults[:10]):
            ResultText = f"{i + 1}. {resultat[0]} {resultat[1]} min {resultat[2]} sec"
            resultLabel = tk.Label(highscoreRoot, text=ResultText)
            resultLabel.pack()
        submitButton = tk.Button(highscoreRoot, text="Exit", command=lambda: self.root.destroy())
        submitButton.pack(pady=10)

    def refreshWindow(self):
        """Uppdaterar fonster 
        inparametarar listan med toppvärden och rooten på fönster
        returnerar nedstägning av fönster
        """

        for i in range(self.size):
            for j in range(self.size):
                btn = self.root.children["!frame"].grid_slaves(row=i, column=j)[0]
                if(self.board[i][j]!=BOMB and self.board[i][j]!=FLAG):
                    btnText = self.board[i][j]
                    btn.config(text=btnText)

    def bombsAround(self,dig, bombs):
        """kollar om spelplanens rutan är noll om ja frav runt och forstatt på dessa spara att du har använt specifik SpelPlan
        inparametrar befintlig(platsen som har använts för att gräva runt), dig, bombs, SpelPlan
        rekusiv  funktion
        """
        digAround = set()
        numOfBombs = 0
        self.checkForNerby(numOfBombs, digAround, dig, bombs)
        return str(searth(dig, bombs))

    def checkForNerby(self,numOfBombs, alreadyDug, dig, bombs):
        """kollar om spelplanens rutan är noll om ja frav runt och forstatt på dessa spara att du har använt specifik SpelPlan
        inparametrar befintlig(platsen som har använts för att gräva runt), dig, bombs, SpelPlan
        rekusiv  funktion
        """
        if dig not in alreadyDug:
            alreadyDug.add(dig)
            i, j = dig
            self.board[i][j] = str(searth(dig, bombs))
            if self.board[i][j] == '0':
                for row in range(i - 1, i + 2):
                    for col in range(j - 1, j + 2):
                        if 0 <= row < self.size and 0 <= col < self.size:
                            self.checkForNerby(numOfBombs, alreadyDug, (row, col),bombs)
