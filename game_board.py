import random
import time
from utils import *

FILL = ' '
FLAG = 'F'
BOMB = 'B'

class GameBoard:

    def __init__(self,size,bombSize):
        
        self.board = [[FILL for _ in range(size)] for _ in range(size)]
        self.size=size
        self.bombSize=bombSize
    
    def __str__(self):
        
        return self.__repr__()

    def __repr__(self):
        """
        Returns a string describing how the game board looks.
        Parameters: self
        Returns: a string describing the game board
        """
        letterCounter = 'A'
        returnValue = ""

        returnValue += '  ┏'
        for i in range(self.size):
            returnValue += "━━━┳"
        returnValue += "━━━┓\n"
        returnValue += '  ┃   ┃'
        for _ in range(self.size):
            returnValue += f' {letterCounter} ┃'
            letterCounter = chr(ord(letterCounter) + 1)
        returnValue += '\n'

        for row in range(self.size):
            returnValue += '  ┣'
            for _ in range(self.size):
                returnValue += "━━━╋"

            returnValue += '━━━┫\n'
            returnValue += f'  ┃ {row + 1} ┃ '
            for col in range(self.size):
                returnValue += self.board[col][row] + ' ┃ '

            returnValue += '\n'

        returnValue += '  ┗'
        for i in range(self.size):
            returnValue += "━━━┻"
        returnValue += "━━━┛\n"

        return returnValue

    def printoutGameOver(self, bombs):

        for row in range(self.size):
            for col in range(self.size):
                if checkBomb(bombs, (row, col)):
                    if(self.board[row][col]!=FLAG):
                        self.board[row][col] = BOMB
        print(self)

    def interpret(self,bombs):
        
        while True:
            userInput = input("Where do you want to dig,(insert cordinates)? ")
            try:
                letter = userInput[0].upper()
                if 'A' <= letter <= chr(ord('A') + self.size - 1) and 1 <= int(userInput[1]) <= self.size:
                    row = ord(letter) - ord('A')
                    col = int(userInput[1]) - 1
                    return row, col
                elif 'X' == letter and 1 <= int(userInput[2]) <= self.size:
                    row = ord(userInput[1].upper()) - ord('A')
                    col = int(userInput[2]) - 1
                    self.flag(row, col)
                    if(self.checkWin(bombs)):
                        return -1,-1
                    print(self)
                elif 'R' == letter and 1 <= int(userInput[2]) <= self.size:
                    row = ord(userInput[1].upper()) - ord('A')
                    col = int(userInput[2]) - 1
                    self.reflag(row, col)
                    print(self)
                elif 'Y'==letter:
                    help()
                    self.interpret(bombs)
                else:
                    print("Utanför spelplanen")
            except (ValueError, IndexError):
                print("Error, value not in bounds")

    def flag(self, rad, kolumn):
       
        self.board[rad][kolumn] = FLAG

    def reflag(self, rad, kolumn):
        
        self.board[rad][kolumn] = FILL
    
    def bombsAround(self, digPlace, bombs):
        """
        indicates the number of bombs around and forwards to check around, 
            receives afterward and sends check(grav, bombs) where it continues until it doesn't find 0
        parameters: grav, bombs, game board
        returns a string
        """
        checkedPlace = set()
        numberOfBombs = 0
        self.checkAround(numberOfBombs, checkedPlace, digPlace, bombs)
        return str(check(digPlace, bombs))

    def checkAround(self,bombNumber, alreadyChecked, digPlace, bombs):
        
        
        if digPlace not in alreadyChecked: #dont enter the boxes the function has already entred
            alreadyChecked.add(digPlace)
            row, col = digPlace
            self.board[row][col] = str(check(digPlace, bombs))
            if self.board[row][col] == '0': #check if its 0 then dig around the 'box'
                for rowRange in range(row - 1, row + 2):
                    for colRange in range(col - 1, col + 2):
                        if 0 <= rowRange < self.size and 0 <= colRange < self.size:
                            self.checkAround(bombNumber, alreadyChecked, (rowRange, colRange), bombs)
    
    def checkWin(self, bombs):
        """
        Checks if player has won(on flags or by not marking the bombs at all, or all the boxes are the same)
        parameters: self and bombs
        returns a boolean true or false
        """
        totalFlags = 0
        stateWin=-1
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == FILL:
                    if checkBomb(bombs, (row,col))==True:
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

            
    def printOutCorrect(self,bombs):
        correctFlags = 0
        wrongFlags=0
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == FLAG:
                    if checkBomb(bombs, (row,col))==True:
                        correctFlags+=1
                    else:
                        wrongFlags+=1
        return correctFlags,wrongFlags