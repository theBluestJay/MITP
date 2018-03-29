import random
### FUNCTIONS

attributes = {"punkty" : 0, "siła" : 0,"budowa" : 0,"zręczność" : 0,"roztropność" : 0,"inteligencja" : 0,"charyzma" : 0 }

#---------------------
def drawPoints():
    attributes["punkty"] = random.randint(40, 91)

#---------------------
def addPoints():
    whichAttr = input("Do której cechy chesz dodać punkty?\n Siła, budowa, zręczność, roztropność, inteligencja, charyzma?")
    if whichAttr.lower() in attributes:
        whichAttr = whichAttr.lower()
        wannaAdd = int(input("Ile punktów chcesz dodać: "))
        if 5 <= attributes[whichAttr] + wannaAdd <= 20:
            attributes[whichAttr] = attributes[whichAttr] + wannaAdd
            attributes["punkty"] -=  wannaAdd
            print(whichAttr.capitalize(), " ma teraz", attributes[whichAttr], "punktów.")
            print("Zostało ci", attributes["punkty"], "punktów")
        else:
            print("Próbujesz dodać nieodpowiednią ilość punktów. Pamiętaj, jeden atrybut może mieć tylko od 5 do 20 punktów.")

#---------------------
def substractPoints():
    whichAttr = input("Od której cechy chesz odjąć punkty?\n Siła, budowa, zręczność, roztropność, inteligencja, charyzma?")
    if whichAttr.lower() in attributes:
        whichAttr = whichAttr.lower()
        wannaSub = int(input("Ile punktów chcesz odjąć: "))
        if 5 <= attributes[whichAttr] - wannaSub <= 20:
            attributes[whichAttr] = attributes[whichAttr] - wannaSub
            attributes["punkty"] += wannaSub
            print(whichAttr.capitalize(), " ma teraz", attributes[whichAttr], "punktów.")
            print("Zostało ci", attributes["punkty"], "punktów")
        else:
            print(
                "Próbujesz odjąć nieodpowiednią ilość punktów. Pamiętaj, jeden atrybut może mieć tylko od 5 do 20 punktów.")

#---------------------
def showStats():
    print("Oto twoje statystyki: ")
    for item in attributes:
        print(item.capitalize(), " = ", attributes[item])

### MAIN ---------------------

drawPoints()
print("Masz", attributes["punkty"], " punktów. Co chcesz zrobić?")
running = True
while running == True:
    print("Co chcesz teraz zrobić: ")		
    action = input(" 1 - dodaj punkty 2 - odejmij punkty 3 - pokaż wszystkie statystyki 4 - zakończ: ")
    if action == "1":
        addPoints()
    elif action == "2":
        substractPoints()
    elif action == "3":
        showStats()
    elif action == "4":
        break