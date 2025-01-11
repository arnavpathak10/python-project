import random
#Defining Game Instruction
print("""Winning Rules of Rock Paper Scissor Game are :\n
Rock vs Paper -> Paper wins
Rock vs Scissor -> Rock wins
Paper vs Scissor -> Scissor wins
--------------------------------------------------""")
#Defining list of choice user have
print("Enter your choice\n 1 - Rock\n 2 - Paper\n 3 - Scissor")

DATA = {1:"Rock",
        2:"Paper", 
        3:"Scissor"}

#function to select choice by user
def player():
    #Taking input by user
    n = int(input("Enter integer from 1 to 3 to select choice : "))
    #loop check that user enter valid number between 1 to 3 or not. 
    # If not enter valid no. then input it again.
    while True:
        if(n<1 or n>3):
           print("Invalid Selection! Try Again")
           n = int(input("Enter integer from 1 to 3 to select choice : "))
           
        else:
            print(f"Your choice is {DATA[n]}")
            break
    return DATA[n]  #Return choice enter by user

#function to select choice by computer
def com_player():
    #computer select random integer from range 1 to 3
    x = random.randint(1,3)
    print(f"Now it's computer turn ---\nComputer selection is {DATA[x]}")

    return DATA[x] #Return choice enter by user

#Defining function to check and declare who wins
def result_declaration(usr, com):
    print(f"**** {usr} vs {com} ****\n")
    if((usr == "Rock" and com == "Paper") or (usr == "Scissor" and com == "Rock") or (usr == "Paper" and com == "Scissor")):
        print("$$Computer Wins$$")
    elif((usr == "Rock" and com == "Rock") or (usr=="Scissor" and com == "Scissor") or (usr=="Paper" and com == "Paper")):
        print("$$It's a tie$$")
    else:
        print("$$You Wins$$")


#loop to re-play game 
while True:
    inp = input("Do you want to play(Y/N)\n>")
    if(inp == "Y" or inp == "y"):
        usr = player()
        com = com_player()
        result_declaration(usr, com)
    else:
        break


