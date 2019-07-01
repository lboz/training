# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:06:53 2019

@author: lb
"""


# Program that guesses a secret number!

# The program works as follows: you (the user) thinks of 
# an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - 
# is its guess too high or too low? Using bisection search,
# the computer will guess the user's secret number!


print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)//2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))
      

# V2

print("Please think of a number between 0 and 100!")
low = 0
high = 100

ans = ((high+low)//2)

rep = input("Is your secret number " + str(ans) + "?" +  
     "\nEnter 'h' to indicate the guess is too high. " +
     "Enter 'l' to indicate the guess is too low. "  +
     "Enter 'c' to indicate I guessed correctly: ")


while rep:
    if rep == "c":
        print('Game over. Your secret number was: ' + str(ans))
        break
    elif rep not in ("c", "l", "h"):
        rep = input("Sorry, I did not understand your input. \n" + 
                    "Is your secret number " + str(ans) + "?" +  
                      "\nEnter 'h' to indicate the guess is too high. " +
                        "Enter 'l' to indicate the guess is too low. "  +
                        "Enter 'c' to indicate I guessed correctly: ")
    else:
        while rep == "l":
            low = ans
            ans = (low + high)//2
            rep = input("Is your secret number " + str(ans) + "?" +  
                        "\nEnter 'h' to indicate the guess is too high. " +
                        "Enter 'l' to indicate the guess is too low. "  +
                        "Enter 'c' to indicate I guessed correctly: ")
        
        while rep == "h":
            high = ans
            ans = (low + high)//2
            rep = input("Is your secret number " + str(ans) + "?" +  
                            "\nEnter 'h' to indicate the guess is too high. " +
                            "Enter 'l' to indicate the guess is too low. "  +
                            "Enter 'c' to indicate I guessed correctly: ")

        

