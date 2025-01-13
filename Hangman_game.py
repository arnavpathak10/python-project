import random
words = ("mango", "apple", "lemon", "orange", "banana", "pomogranate")
ran_word = random.choice(words)
print("\nGuess the word! HINT: word is the name of fruit")
g_word = ""
for _ in range(len(ran_word)):
    g_word+="_"
print(g_word)
guess_word = list(g_word)
print("\nguess the character")
count = 0
while True:
    count+=1
    user_guess = input("Enter desired letter : ")
    if(user_guess in ran_word):
        i = ran_word.index(user_guess)
        guess_word[i] = user_guess
        print(guess_word)

    if(ran_word==" ".join(guess_word)):
        print(f"Congratulation! \n You have successfully guessed in {count} attempts")
        break