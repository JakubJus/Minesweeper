import random
import time

def check(grav, bombs):
    """
    checks at a specific location the number of bombs at a square
    Parameters: grav array and bombs 2D array
    Returns a number indicating how many bombs are nearby
    """
    bombsClose = 0
    for bomb in bombs:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if bomb[0] == grav[0] + i and bomb[1] == grav[1] + j:
                    bombsClose += 1

    if grav in bombs:
        bombsClose -= 1
    return bombsClose

#---------------------------------#

def checkBomb(bombs, digPlace):
    for bomb in bombs:
        if bomb[0] == digPlace[0] and bomb[1] == digPlace[1]:
            return True
    return False

#---------------------------------#

def CheckAlreadyExist(bomber, checkRow, checkCol):
    """
    checks if bombs exist in the same place
    Parameters: bombs, the row, and the column where the bomb is to be placed now
        uses a for loop to check through the entire array
    Returns: boolean 1 or 0
    """
    for bombRow, bombCol in bomber:
        if bombRow == checkRow and bombCol == checkCol:
            return False
    return True

#---------------------------------#

def plantBombs(size,bombSize):
    """
    plants bombs, checks if they exist in the same place
    Parameters: the size of the board
    Returns: array of bombs 
    """
    arrayBomb = []
    i = 0
    while i <bombSize:
        bombRow = random.randint(0, size - 1)
        bombCol = random.randint(0, size - 1)
        if CheckAlreadyExist(arrayBomb, bombRow, bombCol):
            arrayBomb.append((bombRow, bombCol))
            i += 1
    return arrayBomb

#---------------------------------#
def askName():
    try:
        return input("Enter Name: ")
    except IndexError:
        print("Error(IndexError): Try again")
        askName()
#---------------------------------#

def askSize(str,max):
    """
    Fragar användaren om input 
    inparametrar fråga string  och maxvärdet som kan antas
    utparametrar int 
    """
    while True:
        try:
            print("Enter num between 1 -",max)
            print("Enter",str,end=": ")
            test=int(input())
            if test>0 and test<=max:
                return test
            else:
                print("Outside of bounds")
        except ValueError: 
            print("please use digits")

#---------------------------------#

def help():
    print("- Write in cordinates to dig, ex(A1)")
    print("- Use X to flag, X and cordinates ex(XA1)")
    print("- Use R to remove flag, R and cordinates ex(RA1)")
    print("- Use Y to see all commands")

#---------------------------------#

def  welcomeWindow():

    print("MINESWEPPER-Creator Jakub Juszkiewicz\n\n")
    print("Welcome to minesweeper please follow the given instructions")
    help()
    print("- When you enter a SIZE number of the board it is for both columns and rows, ex SIZE=8 8x8grid")
    print("Have fun and good luck!\n")

#---------------------------------#
