file = open("raetsel0.txt","r").read().splitlines()
txt = file[0]
wrds = file[1]
#print(txt)
#print(wrds)

"""erstellt eine Liste von 'txt'"""
text = []
firstLetter = 0
for a in range(0,len(txt)):
   if txt[a] == "," or txt[a] == "." or txt[a] == "!" or txt[a] == "?": 
      text.append(txt[firstLetter:a])
      firstLetter = a
   if txt[a] == " ":
      text.append(txt[firstLetter:a])
      firstLetter = a+1
text.append(txt[firstLetter:len(txt)])
#print(text)

"""erstellt eine Liste von 'wrds'"""
words = []
firstLetter = 0
for b in range(0,len(wrds)):
    if wrds[b] == " ":
      words.append(wrds[firstLetter:b])
      firstLetter = b+1
words.append(wrds[firstLetter:len(wrds)])
#print(words)

"""erstellt eine Kopie von 'words'"""
import copy
wordsRemain = copy.copy(words)
#print(wordsRemain)

"""überprüft, ob das Wort aus der Kopie 'wordsRemain' mit der Lücke in 'text' übereinstimmt"""
def isPair(firstPair,secondPair,n):
    #prüft, ob die Lücke nicht schon ausgefüllt wurde
    if wordsToCheck[n]:
       #sucht, wo Buchstaben in der Lücke vorkommt
       for c in range(0,len(firstPair)):
          if firstPair[c] != "_":
             #prüft, ob der Buchstabe der Lücke gleich dem Buchstaben des Worts an dieser Stelle ist
             if firstPair[c] != secondPair[c]:
                return False
       return True
    return False

"""Liste mit boolean-Werten, die aussagen, ob die Lücken schon ausgefüllt wurden"""
wordsToCheck = [True]*len(text)
oldCounter = []
while True:
    """zählt die möglichen Wörter, die in die Lücke passen"""
    counter = [0]*len(text)
    for d in range(0,len(text)):
       for e in range(0,len(wordsRemain)):
            #prüft, welche Lücken mit den Wörtern zusammenpassen, indem nach gleicher Länge und Buchstaben vergleicht wird
            #1.Fall: Satzanfang
            if d != 0 and (text[d-1] == "." or text[d-1] == "!" or text[d-1] == "?"):
               if len(text[d]) == len(wordsRemain[e]) and isPair(text[d],wordsRemain[e],d) and ord(wordsRemain[e][0]) >= 65 and ord(wordsRemain[e][0]) <= 90:
                  #wurde ein Wort gefunden, soll erst geschaut werden, ob es nicht schon einmal gezählt wurde, damit der counter das Wort nicht mehrfach zählt
                  for f in range(0,e):
                     if wordsRemain[e] == wordsRemain[f]:
                        break
                  #ist das nicht der Fall, wird der counter von der Lücke um 1 erhöht
                  else:
                     counter[d] += 1
            #2.Fall: kein Satzanfang
            elif len(text[d]) == len(wordsRemain[e]) and isPair(text[d],wordsRemain[e],d):
               #wurde ein Wort gefunden, soll erst geschaut werden, ob es nicht schon einmal gezählt wurde, damit der counter das Wort nicht mehrfach zählt
               for f in range(0,e):
                  if wordsRemain[e] == wordsRemain[f]:
                     break
               #ist das nicht der Fall, wird der counter von der Lücke um 1 erhöht
               else:
                  counter[d] += 1       
    #print(counter)

    """Bedingung"""
    #wenn der counter bei allen Lücken auf 0 gesetzt ist, sind alle Lücken mit Buchstaben ausgefüllt worden
    #es soll nun die while-Schleife verlassen werden und die restlich Lücken ohne Buchstaben ausgefüllt werden
    if counter == [0]*len(text):
       break

    #wenn sich der counter zwei mal wiederholen sollte, wird die while-Schleife auch verlassen, um Endlosschleifen zu vermeiden
    elif oldCounter == counter:
       break

    """füllt die passenden Lücken aus und entfernt sie von der Kopie 'wordsRemain'"""
    g = 0
    while g < len(wordsRemain):
        for h in range(0,len(text)):
            #prüft, ob Länge und Buchstabe gleich sind und nur ein Wort in Fragen kommen kann
            #1.Fall: Satzanfang
            if h != 0 and (text[h-1] == "." or text[h-1] == "!" or text[h-1] == "?"):
               if len(wordsRemain[g]) == len(text[h]) and isPair(text[h],wordsRemain[g],h) and ord(wordsRemain[g][0]) >= 65 and ord(wordsRemain[g][0]) <= 90 and counter[h] == 1:
                  #die Lücke wird mit dem Wort ersetzt
                  #das Wort wird von der Kopie entfernt
                  #das Lücke wird in der boolean-Liste als schon ausgefüllt markiert
                  text[h] = words[words.index(wordsRemain[g])]
                  wordsRemain.remove(wordsRemain[g])
                  wordsToCheck[h] = False
                  break
            #2.Fall: kein Satzanfang
            elif len(wordsRemain[g]) == len(text[h]) and isPair(text[h],wordsRemain[g],h) and counter[h] == 1:
               #die Lücke wird mit dem Wort ersetzt
               #das Wort wird von der Kopie entfernt
               #das Lücke wird in der boolean-Liste als schon ausgefüllt markiert
               text[h] = words[words.index(wordsRemain[g])]
               wordsRemain.remove(wordsRemain[g])
               wordsToCheck[h] = False
               break
            elif h == len(text)-1:
               g += 1
    #print(text)
    #print(wordsRemain)
    oldCounter = counter

"""füllt die restlichen Lücken mit den noch übrigen Wörtern aus"""
for i in range(0,len(text)):
    #prüft, ob die Lücke mit einem Unterstrich beginnt
    if text[i][0] == "_":
       #1.Fall: Satzanfang
       if i != 0 and (text[i-1] == "." or text[i-1] == "!" or text[i-1] == "?"):
          for j in range(0,len(wordsRemain)):
             #prüft, ob die Länge übereinstimmt und Wort mit einem Großbuchstaben beginnt
             if len(text[i]) == len(wordsRemain[j]) and ord(wordsRemain[j][0]) >= 65 and ord(wordsRemain[j][0]) <= 90:
                text[i] = words[words.index(wordsRemain[j])]
       #2.Fall: kein Satzanfang
       else:
          for j in range(0,len(wordsRemain)):
             #prüft, ob die Länge übereinstimmt und Wort mit einem Kleinbuchstaben beginnt
             if len(text[i]) == len(wordsRemain[j]):
                text[i] = words[words.index(wordsRemain[j])]
#print(text)

"""konvertiert die Liste in einen Text"""
output = ""
for k in range(0,len(text)):
   if k == len(text)-1:
      output += text[k]
   elif text[k+1] == "," or text[k+1] == "." or text[k+1] == "!" or text[k+1] == "?":
      output += text[k]
   else:
      output += text[k] + " " 
print(output)
