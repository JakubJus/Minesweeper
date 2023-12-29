FILE='Highscores.txt'

def higscoreFile(listOfValues):
    """
    Oppnar fil om den finns annars skapas det en ny med 10 satta varden
        inparametar filnman och listOfValues
    """
    try:
        with open(str(FILE), 'r') as fil:
            for line in fil:
                nameMinutesSeconds = line.strip().split(': ')
                try:
                    if len(nameMinutesSeconds) == 3:
                        name = nameMinutesSeconds[0]
                        minutes = int(nameMinutesSeconds[1])
                        seconds = int(nameMinutesSeconds[2])
                        listOfValues.append((name, minutes, seconds))
                    else:
                        print("Coudnt read\n")
                except:
                    print("Coudnt read\n")
        print("Opening file")
    except FileNotFoundError:
        print("File dosent exist")
        open(str(FILE), "x").close()
        print("Have made new file")
        for _ in range(10):
            name = "N.N"
            minutes = 999
            seconds = 99
            listOfValues.append((name, minutes, seconds))

def saveFile(listOfValues):
    """
    skriver till filen och stänger hela proceduren
    inparametar filnman och listOfValues
    """
    with open(str(FILE), 'w') as fil:
        for values in listOfValues:
            minutes = str(values[1])
            seconds = str(values[2])
            print(values[0] + ":", minutes, ":", seconds, file=fil)
