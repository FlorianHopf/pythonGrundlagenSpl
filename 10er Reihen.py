for z in range(1, 11):
  
  print("Zahlen von 1 bis 100: ", z, "er Reihe")
  
  for n in range(z, 101, z):
    print(n, end=", ")
  
  print()
  print("-------------------------------------")