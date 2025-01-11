import random
A = int(input("Enter an lower bound : "))
B = int(input("Enter an upper bound : "))
x = random.randint(A,B)
count = 0
chances = int(input("Enter the number of chances to guess : "))
while True:
    if(count>(chances-1)):
        print(f"Sorry! Try next time, you have exceeds the total number of chances {chances}")
        break
    guess = int(input(f"Enter any integer number in the range {A} and {B} : "))
    if(guess == x):
        print("Congratulations!")
        count+=1
        print(f"You have successfully guessed in {count} try")
        break
    elif(x<guess<=B):
        print("Try Again! You guessed too high")
        count+=1
    elif(A<=guess<x):
        print("Try Again! You guessed too small")
        count+=1
#Time_complexity = O(chances)
#Auxiliary_complexity = O(1)