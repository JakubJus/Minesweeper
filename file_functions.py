FILE="Points.txt"

def higscoreFile(filename, listOfValues):
    
    try:
        with open(str(filename), 'r') as fil:
            for line in fil:
                nameMinutesSeconds = line.strip().split(': ')
                try:
                    if len(nameMinutesSeconds) == 3:
                        name = nameMinutesSeconds[0]
                        minutes = int(nameMinutesSeconds[1])
                        seconds = int(nameMinutesSeconds[2])
                        listOfValues.append((name, minutes, seconds))
                    else:
                        print("Coundt read\n")
                except:
                    print("Coundt read\n")
        print("Opening file")
    except FileNotFoundError:
        print("File dosent exist")
        open(str(filename), "x").close()
        print("Have made new file")
        for _ in range(10):
            name = "N.N"
            minutes = 999
            seconds = 99
            listOfValues.append((name, minutes, seconds))

def saveFile(listOfValues, filename):
    
    with open(str(filename), 'w') as fil:
        for values in listOfValues:
            minutes = str(values[1])
            seconds = str(values[2])
            print(values[0] + ":", minutes, ":", seconds, file=fil)

def printHighscoreList(namn, minuter, sekunder):
    """
    prints the top 10 results from the file and (if existing results are better) the existing result
    parameters: name, minutes, seconds
    """
    filename = FILE
    listOfValues = []
    higscoreFile(filename, listOfValues)
    for i in range(10):
        if listOfValues[i][1] > minuter or (listOfValues[i][1] == minuter and listOfValues[i][2] > sekunder):
            listOfValues.insert(i, (namn, minuter, sekunder))
            listOfValues.pop()
            break

    print("Highscores")
    for i, score in enumerate(listOfValues[:10]):
        print(i + 1, score[0], "time", score[1], "min", score[2], "sec")
    saveFile(listOfValues, filename)