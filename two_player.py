'''
1  for rock
-1 for paper
0 for scissor
'''

computer = 0
youstr = input("Enter Your choice:")
youDict = {"rock" : 1, "paper" : -1, "scissor" : 0}
reverseDict = {1 : "rock", -1 : "paper", 0 : "scissor"}
you = youDict[youstr]


print(f"You chose : {reverseDict[you]} \nMe chose : {reverseDict[computer]} ")


if(computer == you):
    print("It's a draw")

else:   
    if(computer == -1 and you == 1):
        print("You lose")

    elif(computer == -1 and you == 0):
        print("You win")

    elif(computer == 1 and you == -1):
        print("You win")

    elif(computer == 1 and you == 0):
        print("You lose")

    elif(computer == 0 and you == -1):
        print("You lose")

    elif(computer == 0 and you == 1):
        print("You win")

    else:
        print("Something went wrong")