summe = 0
n = 1
while n <= 10:
  summe = summe + n
  print(n, end=", ")
  n += 1
  if(n >= 10):
    break
  
print(summe)