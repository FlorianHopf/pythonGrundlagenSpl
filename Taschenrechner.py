print("Taschenrechner (+; -; *; /; **)")

zahl1 = float(input("Bitte die 1. Zahl eingeben: "))
rechenzeichen = input("+, -, *, /, ** :")
zahl2 = float(input("Bitte die 2. Zahl eingeben: "))
  
if(rechenzeichen == "+"):
  summe = zahl1 + zahl2
  print("Summe = ", summe)
  
if(rechenzeichen == "-"):
  differenz = zahl1 - zahl2
  print("Differenz = ", differenz)
  
if(rechenzeichen == "*"):
  produkt = zahl1 * zahl2
  print("Produkt = ", produkt)
  
if(rechenzeichen == "/"):
  if(zahl2 != 0):
    quotient = zahl1 / zahl2
    print("Quotient = ", quotient)
  else:
    print("Fehler: Division durch Null nicht moeglich")
  
if(rechenzeichen == "**"):
  hochzahl = zahl1 ** zahl2
  print("Quadrierung = ", hochzahl)