import random
import string

def generate_password(min_length, var, is_digit = True, is_splchar = True):
    alphabet = string.ascii_letters
    digit = string.digits
    special_char = string.punctuation

    characters = alphabet   #By default password generated with alphabet
    if(is_digit):   #if user input is true then digit are included in their password
        characters += digit
    if(is_splchar):     #if user input is true then special character are included in their password
        characters += special_char 

    password = ""     #contains generated password
    password+=var     #concatenate desired character input taken by user
    has_digit = False
    has_spe_char = False 

    while not(len(password)>=min_length):
        char = random.choice(characters)
        password += char

        if(is_digit) and not(has_digit) and len(password)<min_length:
            password+=random.choice(digit)
            has_digit = True
        
        if(is_splchar) and not(has_spe_char) and len(password)<min_length:
            password+=random.choice(special_char)
            has_spe_char = True


    return password 

while True:
    class length_error(Exception):
        pass
    try:
        min_length = int(input("Enter length of password to generate : "))
        inp = input("Do you want to add any character in starting of password (y/n) by default No : ")
        var = ""
        if(inp.lower()=="y" or inp.lower()=="yes"):
            var = input("Enter desired character : ")
            if(len(var)>(min_length)):
                raise length_error("Length of word is greater than length of password to generate")

        digi = input("Do you want digits in password (y/n) (By Default its No) : ")
        spl_char = input("Do you want special characters in password (y/n) (By Default its No) : ")

        is_digit = False
        is_splchar = False
        if(digi.lower()=="y" or digi.lower()=="yes"):
            is_digit = True
        if(spl_char.lower()=="y" or spl_char.lower()=="yes"):
            is_splchar = True

        pwd = generate_password(min_length, var, is_digit, is_splchar)
        print(f"Your Generated Password is {pwd}")
        break

    except length_error as er:
        print(er,"\n")
