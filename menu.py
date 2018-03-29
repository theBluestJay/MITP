###FUNCTIONS

scores = [("Ala",10), ("Monika", 5), ("Iza",7), ("Adam", 7)]

def showTopScores():
    print("Oto najwyższe wyniki: ")
    place = 1
    sortedScores = sorted(scores, key=lambda scores: scores[1], reverse=True)
    for item in sortedScores:
        print(place, ".", item[0], " : ", item[1])
        place += 1

def startNewGame():
    print("Nowa gra...")
    playerName = input("Podaj swoje imię: ")
    newScore = (playerName.capitalize(), 0)
    scores.append(newScore)

def menu():
    running = True
    while running == True:
        print("Co chcesz zrobić?")
        action = input("Start - zacznij nową grę, Top - pokaż najwyższe wyniki, End - zakończ: ")
        if action.lower() == "start":
            startNewGame()
        elif action.lower() == "top":
            showTopScores()
        elif action.lower == "end":
            exit(1)
            ## to gówno nie działa ><

###MAIN
menu()

