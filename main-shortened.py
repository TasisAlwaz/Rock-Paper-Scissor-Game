import random

computer = random.choice([-1, 0, 1])

youstr = input("Enter Your choice (rock/paper/scissor): ").lower()

youDict = {"rock": 1, "paper": -1, "scissor": 0}
reverseDict = {1: "rock", -1: "paper", 0: "scissor"}

# convert input to number
you = youDict[youstr]

print(f"You chose : {reverseDict[you]} \nComputer chose : {reverseDict[computer]}")

# check result
if computer == you:
    print("It's a tie!")
elif (computer - you) == -1 or (computer - you) == 2:
    print("You lose")
else:
    print("You win")
