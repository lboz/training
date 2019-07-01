# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:52:37 2019

@author: Lia Bozneanu
"""

# Hangman game

# -----------------------------------
# Requirements for the game:
'''
The computer selects a word at random from the list of available words 
(words.txt). 

The game is interactive; the flow of the game goes as follows:
  - At the start of the game, let the user know how many letters the computer's
    word contains.
  - Ask the user to supply one guess (i.e. letter) per round.
  - The user should receive feedback immediately after each guess about whether
    their guess appears in the computer's word.
  - After each round, the computer displays to the user the partially guessed
    word so far, as well as the position of the letters that the user has not 
    yet guessed.
    
Some additional rules of the game:
-   A user is allowed 8 guesses. Make sure to remind the user of how many
    guesses s/he has left after each round. Assume that players will only ever
    submit one character at a time (A-Z).
-   A user loses a guess only when s/he guesses incorrectly.
-   If the user guesses the same letter twice, do not take away a guess - 
    instead, print a message letting them know they've already guessed that 
    letter and ask them to try again.
-   The game ends when the user constructs the full word or runs out of 
    guesses. If the player runs out of guesses (s/he "loses"), reveal the word
    to the user when the game ends.
'''

import random

WORDLIST_FILENAME = "C:/Users/User/Documents/Lia/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if lettersGuessed in secretWord:
        return True
    else:
        return False

    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    i = 0
    foundL = []
    while i < len(secretWord):
        if secretWord[i] in lettersGuessed:
            foundL.append(secretWord[i])
        else:
            foundL.append("_")
        i+=1
    y = ''.join(foundL) 
    return y


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alfabet = string.ascii_lowercase
    i=0
    newL = []
    while i < len(alfabet):
        if alfabet[i] in lettersGuessed:
            newL.append('')
        else:
            newL.append(alfabet[i])
        i+=1
    y = ''.join(newL)     
    return y


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many letters the 
      secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman! \nI am thinking of a word that is " +
          str(len(secretWord)) + " letters long.")
    lettersGuessed = []
    import string
    n = 8
    while n > 0:
        print("-----------\nYou have " + str(n) + " guesses left")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        ggw = getGuessedWord(secretWord, lettersGuessed)
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + ggw)
            lettersGuessed.append(guess)
        elif guess not in secretWord:
            print("Oops! That letter is not in my word: " + ggw)
            lettersGuessed.append(guess)
            n-=1
        else: 
            lettersGuessed.append(guess)
            ggw = getGuessedWord(secretWord, lettersGuessed)
            print("Good Guess: " + ggw)
            if ggw == secretWord:
                return print("-----------\nCongratulations, you won!")
                break
            else:
                n+=0
    return print("-----------\nSorry, you ran out of guesses. The word was " +
                 secretWord)           


secretWord = chooseWord(wordlist).lower()
# print(secretWord)
hangman(secretWord)