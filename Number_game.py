import random
lst = []
last = 0

def player1():
    global last
    rn_int = random.randint(1,4)
    for _ in range(rn_int):
        lst.append((last+1))
        last = lst[-1]
        if(lst[-1]==21):
            print("Congratulations! \nYou Won")
            break
    else:
        player2()

def player2():
    print("Your turn\nOrder of input after computer's turn is",lst)
    n = int(input("\nHow many number want to enter between 1 to 4 : "))
    while(n>4):
        print("invalid number! Enter Again")
        n = int(input("How many number want to enter between 1 to 4 : "))

    for _ in range(n):
        global last
        num = int(input(f"Enter {n} consecutive number after {last} : "))
        if(last==num-1):
            lst.append(num)
            last = num
            if(num==21):
                print("\nYou lose! Better luck next time!")
                break
        else:
            print("Sorry! you lose. Not Enter Consecutive Number")
            break
    else:
        player1()
    

def calling_instruction():
        print("Player 1 is Computer")
        chance = input("Enter F or S to take first chance or second chance\n>")
        if(chance == "S" or chance == "s"):
            player1()
        else:
            player2()
    
while True:
    inp = input("Do you want to continue(Yes/No)\n>")
    if(inp.lower() == "yes" or "y"):
        calling_instruction()
        lst = []
        last = 0
    else:
        break

