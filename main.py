import random
fruits = ["cherry", " bell", "lemon","orange","star","skull"]
money = 1.00
print("Welcome to the fruit machine") 
print("You have £1")
print("Each go costs 20p")
print("If you roll two of the same symbol you win 50p")
print("If you roll three of the same symbol you win £1")
print("If you roll three bells you win £5")
print("If you roll two skulls you lose £1")
print("If you roll three skulls you lose all your money")
print("You can choose to quit at any point")
print("Press enter to play")
input()
print("Rolling...")

f1 = random.choice(fruits)
f2 = random.choice(fruits)
f3 = random.choice(fruits)
print(f1,f2,f3)
while True:
  if f1 == f2 and f2 == f3:
    print("You won £1")
    money = money + 1.00
    break
  elif f1 == f2 or f2 == f3 or f1 == f3:
    money = money + 0.50
    print("you won 50p")