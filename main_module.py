from game_board import GameBoard
from file_functions import higscoreFile, saveFile, printHighscoreList
from utils import*

def mainloop():
    """
    1. initing, and printing instructions
    2. pritning gameboard
    3. Understadning an input
    4. checking lost->true-> end program
    5. check any bombs around
    6. check win->ture-> end program
    7. repeat from stage 2
    """

    welcomeWindow()
    size = askSize("Size",9)
    bombSize = askSize("Number of bombs",(size*size))

    activeGame = GameBoard(size,bombSize)
    bombs = plantBombs(size,bombSize) 
    dig = [] 
    startTime = time.time()


    while True: 
        print(activeGame)
        dig = activeGame.interpret(bombs)
        if checkBomb(bombs, dig):
            activeGame.printoutGameOver(bombs)
            correctFlaged,wronglyFlaged=activeGame.printOutCorrect(bombs)
            print("You lost")
            print("You flaged correctly",correctFlaged,"out of",bombSize,"Bombs")
            print("You flaged totaly",correctFlaged+wronglyFlaged)
            break
        activeGame.board[dig[0]][dig[1]] = activeGame.bombsAround(dig, bombs)
        
        if activeGame.checkWin(bombs):
            print(activeGame)
            print("Congratulation! You won!")
            endTime = time.time()
            elapsedSeconds = int(endTime - startTime)
            minutes = elapsedSeconds // 60
            seconds = elapsedSeconds % 60
            name = askName()
            printHighscoreList(name, minutes, seconds)
            break