file = open("spielstaerken1.txt","r").read().splitlines()

"""Anzahl der Spieler"""
n = int(file[0])
#print(n)

"""Spielstärken der Spieler"""
strengths = []
for a in range(1,len(file)):
    strengths.append(int(file[a]))
#print(strengths)

"""Spieler mit der größten Spielstärke"""
strongest = strengths.index(max(strengths))+1
#print(strongest)

from random import *
"""legt den Gewinner nach dem Urnenmodell fest"""
def winner(playingStrength1,playingStrength2):
    r = random()
    if r <= playingStrength1/(playingStrength1+playingStrength2):
        return True
    if r > playingStrength1/(playingStrength1+playingStrength2):
        return False

"""legt den Gewinner nach fünfmaligem Wiederholen des Urnenmodells fest"""
def winnerBestOfFive(playingStrength1,playingStrength2):
    counter1 = 0
    counter2 = 0
    for b in range(1,5):
        r = random()
        if r <= playingStrength1/(playingStrength1+playingStrength2):
            counter1 += 1
        if r > playingStrength1/(playingStrength1+playingStrength2):
            counter2 += 1
    if counter1 > counter2:
        return True
    else:
        return False

numWinnerLiga = 0
numWinnerKO = 0
numWinnerKOBestOfFive = 0
#Anzahl Wiederholungen
c = 10000
import copy
from random import shuffle
for d in range(1,c+1):
    """Liga"""
    #zählt wie oft die Spieler gewinnen im Jeder gegen Jeden Modus
    counter = [0]*n
    for e in range(0,n-1):
        for f in range(e+1,n):
            if winner(strengths[e],strengths[f]) == True:
                counter[e] += 1
            else:
                counter[f] += 1
    #der Sieger der Liga ist der Spieler mit den meisten Siegen
    largestNumber = max(counter)
    winnerLiga = counter.index(largestNumber)+1
    #der Sieger der Liga wird mit dem Spielstärksten vergleicht, bei Übereinstimmung wird der Zähler um 1 erhöht
    if winnerLiga == strongest:
        numWinnerLiga += 1
    #print(counter)
    #print(winnerLiga)

    """K.O."""
    #Kopie der Spielstärken ist erforderlich, da Verlierer gestrichen werden
    strengthsCopy = copy.copy(strengths)
    #nach Beschreibung der Turniervarianten sollen verschiedene Pläne getestet werden
    shuffle(strengthsCopy)
    #Indexe müssen gespeichert werden, da sich bei Streichen der Verlierer aus der Kopie die Indexe der Gewinner verändern
    indexes = list(range(n))
    limit = n
    while limit >= 2:
        for g in range(0,limit//2):
            if winner(strengthsCopy[g],strengthsCopy[g+1]) == True:
                #Spieler 2 wird aus der Kopie gelöscht
                del strengthsCopy[g+1]
                del indexes[g+1]
            else:
                #Spieler 1 wird aus der Kopie gelöscht
                del strengthsCopy[g]
                del indexes[g]
        #print(strengthsCopy)
        #print(indexes)
        #es sind nur noch halb so viele Spieler übrig
        limit = limit//2
    #der Sieger ist der Spieler der übrig bleibt, Spielernummer ist indexes[0]+1
    winnerKO = indexes[0]+1
    #der Sieger des K.O. wird mit dem Spielstärksten vergleicht, bei Übereinstimmung wird der Zähler um 1 erhöht
    if winnerKO == strongest:
        numWinnerKO += 1
    #print(winnerKO)

    """K.O.×5"""
    #Wiederholung des K.O., aber hier mit winnerBestOfFive()-Funktion
    strengthsCopy2 = copy.copy(strengths)
    shuffle(strengthsCopy2)
    indexes = list(range(n))
    limit = n
    while limit >= 2:
        for h in range(0,limit//2):
            if winnerBestOfFive(strengthsCopy2[h],strengthsCopy2[h+1]) == True:
                del strengthsCopy2[h+1]
                del indexes[h+1]
            else:
                del strengthsCopy2[h]
                del indexes[h]
        #print(strengthsCopy2)
        #print(indexes)
        limit = limit//2
    winnerKOBestOfFive = indexes[0]+1
    if winnerKOBestOfFive == strongest:
        numWinnerKOBestOfFive += 1
    #print(winnerKOBestOfFive)

"""Berechnung der Gewinn-Wahrscheinlichkeit des Spielstärksten im Durchschnitt"""
i = numWinnerLiga/c
j = numWinnerKO/c
k = numWinnerKOBestOfFive/c
print("Gewinnwahrscheinlichkeit Liga: "+str(i))
print("Gewinnwahrscheinlichkeit K.O.: "+str(j))
print("Gewinnwahrscheinlichkeit K.O.×5: "+str(k))

if max(i,j,k) == i:
    print("Liga ist die geeignetste Turniervariante")
elif max(i,j,k) == j:
    print("K.O. ist die geeignetste Turniervariante")
elif max(i,j,k) == k:
    print("K.O.×5 ist die geeignetste Turniervariante")
