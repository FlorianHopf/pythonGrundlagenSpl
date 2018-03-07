import random

minZahl = int(input("Geben Sie die Anfangszahl ein: "))
maxZahl = int(input("Geben Sie die Endzahl ein: "))
versuche = int(input("Geben Sie die Versuche ein: "))

zufallszahl = random.randint(minZahl,maxZahl)

print("Zahlenraten - errate meine Zahl zwischen", minZahl, "und", maxZahl)

gewonnen = False

while versuche > 0:
  zahl = int(input("Welche Zahl? "))
  if(zahl == zufallszahl): 
    print("Glückwunsch! Sie haben die Zahl errraten.")
    print("Du hattest noch", versuche, "übrig")
    break
  elif(zahl < zufallszahl):
    print("Leider nein! Die gesuchte Zahl ist größer.")
    versuche -= 1
    print("Du hast noch", versuche, "übrig")
  elif(zahl > zufallszahl):
    print("Leider nein! Die gesuchte Zahl ist kleiner.")
    versuche -= 1
    print("Du hast noch", versuche, "übrig")