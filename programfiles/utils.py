import random

def checkBomb(bombs,digPlace):
    """kollar om bombs finns på plats 
    Inparameter:bombs, raden och kolumnen som bomben ska bli placerad nu på 
    Returnerar: booleskt 1 eller 0"""
    for bomb in bombs:
        if bomb[0] == digPlace[0] and bomb[1] == digPlace[1]:
            return False
    return True

def plantBombs(bombSize,size):
    
    bombs = []
    i = 0
    while i < bombSize:
        bombRow = random.randint(0, size - 1)
        bombCol = random.randint(0, size - 1)
        if checkBomb(bombs,(bombRow, bombCol)):
            bombs.append((bombRow, bombCol))
            i += 1
    return bombs



def searth(dig, bombs):
    """kollar på en specifk plats antalet bombs vid en SpelPlan
    inparametrar  dig array och bombs 2d array
    returnarar en siffra  på hur många bombs som finns i närheten
    """
    bombsAround = 0
    for bomb in bombs:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if bomb[0] == dig[0] + i and bomb[1] == dig[1] + j:
                    bombsAround += 1

    if dig in bombs:
        bombsAround -= 1
    return bombsAround
