file = open("puzzle0.txt","r").read().splitlines()

temp = []
for x in range(2,11):
    counter = 0
    for y in range(0,len(file[x])):
        if file[x][y] == " ":
            temp.append(int(file[x][counter:y]))
            counter = y+1
        elif y == len(file[x])-1:
            temp.append(int(file[x][counter:len(file[x])]))
#print(temp)

cards = []
for z in range(0,27,3):
    cards.append(temp[z:z+3])
#print(cards)

def findSolution():
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                if i != j and i != k and j != k:
                    firstCard = cards[i]
                    secondCard = cards[j]
                    thirdCard = cards[k]
                    for l in range(0,3):
                        for m in range(0,3):
                            for n in range(0,3):
                                if l == 0:
                                    firstCardFirstFigure = firstCard[0]
                                    firstCardSecondFigure = firstCard[1]
                                    firstCardThirdFigure = firstCard[2]
                                elif l == 1:
                                    firstCardFirstFigure = firstCard[1]
                                    firstCardSecondFigure = firstCard[2]
                                    firstCardThirdFigure = firstCard[0]
                                elif l == 2:
                                    firstCardFirstFigure = firstCard[2]
                                    firstCardSecondFigure = firstCard[0]
                                    firstCardThirdFigure = firstCard[1]
                                if m == 0:
                                    secondCardFirstFigure = secondCard[0]
                                    secondCardSecondFigure = secondCard[1]
                                    secondCardThirdFigure = secondCard[2]
                                elif m == 1:
                                    secondCardFirstFigure = secondCard[1]
                                    secondCardSecondFigure = secondCard[2]
                                    secondCardThirdFigure = secondCard[0]
                                elif m == 2:
                                    secondCardFirstFigure = secondCard[2]
                                    secondCardSecondFigure = secondCard[0]
                                    secondCardThirdFigure = secondCard[1]
                                if n == 0:
                                    thirdCardFirstFigure = thirdCard[0]
                                    thirdCardSecondFigure = thirdCard[1]
                                    thirdCardThirdFigure = thirdCard[2]
                                elif n == 1:
                                    thirdCardFirstFigure = thirdCard[1]
                                    thirdCardSecondFigure = thirdCard[2]
                                    thirdCardThirdFigure = thirdCard[0]
                                elif n == 2:
                                    thirdCardFirstFigure = thirdCard[2]
                                    thirdCardSecondFigure = thirdCard[0]
                                    thirdCardThirdFigure = thirdCard[1]

                                for p in range(0,9):
                                    fourthCard = cards[p]
                                    if p != i and p != j and p != k:
                                        for q in range(0,3):
                                            fourthCardFirstFigure = fourthCard[q]
                                            if q == 2:
                                                fourthCardSecondFigure = fourthCard[0]
                                            else:
                                                fourthCardSecondFigure = fourthCard[q+1]

                                            if fourthCardFirstFigure == firstCardSecondFigure*(-1) and fourthCardSecondFigure == secondCardFirstFigure*(-1):
                                                for r in range(0,9):
                                                    fifthCard = cards[r]
                                                    if r != i and r != j and r != k and r != p:
                                                        for s in range(0,3):
                                                            fifthCardFirstFigure = fifthCard[s]
                                                            if s == 2:
                                                                fifthCardSecondFigure = fifthCard[0]
                                                            else:
                                                                fifthCardSecondFigure = fifthCard[s+1]
        
                                                            if fifthCardFirstFigure == secondCardSecondFigure*(-1) and fifthCardSecondFigure == thirdCardFirstFigure*(-1):
                                                                for t in range(0,9):
                                                                    sixthCard = cards[t]
                                                                    if t != i and t != j and t != k and t != p and t != r:
                                                                        for u in range(0,3):
                                                                            sixthCardFirstFigure = sixthCard[u]
                                                                            if u == 2:
                                                                                sixthCardSecondFigure = sixthCard[0]
                                                                            else:
                                                                                sixthCardSecondFigure = sixthCard[u+1]
        
                                                                            if sixthCardFirstFigure == thirdCardSecondFigure*(-1) and sixthCardSecondFigure == firstCardFirstFigure*(-1):
                                                                                for a in range(0,9):
                                                                                    seventhCard = cards[a]
                                                                                    if a != i and a != j and a != k:
                                                                                        if a != p and a != r and a != t:
                                                                                            for b in range(0,3):
                                                                                                seventhCardFirstFigure = seventhCard[b]

                                                                                                if seventhCardFirstFigure == firstCardThirdFigure*(-1):
                                                                                                    for c in range(0,9):
                                                                                                        eighthCard = cards[c]
                                                                                                        if c != i and c != j and c != k:
                                                                                                            if c != p and c != r and c != t:
                                                                                                                if c != a:
                                                                                                                    for d in range(0,3):
                                                                                                                        eighthCardFirstFigure = eighthCard[d]

                                                                                                                        if eighthCardFirstFigure == secondCardThirdFigure*(-1):
                                                                                                                            for e in range(0,9):
                                                                                                                                ninthCard = cards[e]
                                                                                                                                if e != i and e != j and e != k:
                                                                                                                                    if e != p and e != r and e != t:
                                                                                                                                        if e != a and e != c:
                                                                                                                                            for f in range(0,3):
                                                                                                                                                ninthCardFirstFigure = ninthCard[f]

                                                                                                                                                if ninthCardFirstFigure == thirdCardThirdFigure*(-1):
                                                                                                                                                    return firstCard,secondCard,thirdCard,l,m,n,fourthCard,fifthCard,sixthCard,q,s,u,seventhCard,eighthCard,ninthCard,b,d,f
    return False
x = findSolution()
if x == False:
    print("Es gibt keine Lösung")
else:
    print(x)
