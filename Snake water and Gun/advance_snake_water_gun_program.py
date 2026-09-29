import random
choices = ["snake","water","gun"]
botinput = random.choice(choices)

playerinput = input("Choose Snake , Water or Gun:- \n").lower().replace(" ","")
winning_combinations = {
    ("snake" , "water"),
    ("water" , "gun"),
    ("gun" , "snake")
}

if playerinput not in choices:
    print("Invalid Input")
elif playerinput == botinput:
    print("Draw")
elif (playerinput,botinput) in winning_combinations:
    print("You won!")
else:
    print("Computer Won!")