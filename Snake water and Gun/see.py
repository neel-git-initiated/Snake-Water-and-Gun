import random
# player = random.randint(1,3)
bot = random.randint(4,6)
if bot == 4:
    botinput = "snake"
elif bot == 5:
    botinput = "water"
elif bot == 6:
    botinput = "gun"
else:
    print("nothing")


playerinputraw = input("Choose Snake,Water or Gun: \n")
playerinputraw2 = playerinputraw.lower()
playerinput = playerinputraw2.replace(" ","")


if playerinput == "snake" and botinput == "snake":
    print("Draw")
elif playerinput == "water" and botinput == "water":
    print("Draw")
elif playerinput == "gun" and botinput == "gun":
    print("Draw")
elif playerinput == "snake" and botinput == "water":
    print("You won")
elif playerinput == "water" and botinput == "snake":
    print("Computer won")
elif playerinput == "gun" and botinput == "snake":
    print("You won")
elif playerinput == "snake" and botinput == "gun":
    print("Computer won")
elif playerinput == "water" and botinput == "gun":
    print("You won")
elif playerinput == "gun" and botinput == "water":
    print("Computer won")
else:
    print("Invalid input")
    
# if player == 1:
#     print(True)
# else:
#     print(False)

# if bot == 4:
#     print(True)
# else:
#     print(False)
