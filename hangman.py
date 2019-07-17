#!/usr/bin/env python3

"""
File: hangman.py
Name:

A python implementation of hangman
Concepts covered: Strings, if/else, while, functions
"""
from time import sleep
import random
import sys

def main(player_preference,lives,success,letter1,letter2,letter3,letter4,letter5,letter6,lettersguessed,letter1guessed,letter2guessed,letter3guessed,letter4guessed,letter5guessed,letter6guessed):
    # Code here
    player_preference = int(input("Would you like to type your own word or use the premade word? 1:First option. 2:Second option;")) 
    if (player_preference = 1):
        input
    elif (player_preference = 2):
        com_word = ("Sphinx")
        while(success==1):
            print("You have " + str(lives) + "left")
            print("The word is 6 letters long")
            guess = input("Guess a letter;")
            if guess == "s":
                letter1guessed = True
                lettersguessed += 1
            if guess == "p":
                letter2guessed = True
            if guess == "h":
                letter3guessed = True
                lettersguessed += 1
            if guess == "i":
                letter4guessed = True
                lettersguessed += 1
            if guess == "n":
                letter5guessed = True
                lettersguessed += 1
            if guess == "x":
                letter6guessed = True
                lettersguessed += 1
def checkWin(guessed_letters):
    # Code here

if __name__ == "__main__":
    main()
#variables
player_preference = 0
lives = 5
success = 0
letter1 = "s"
letter2 = "p"
letter3 = "h"
letter4 = "i"
letter5 = "n"
letter6 = "x"
lettersguessed = 0
letter1guessed = False
letter2guessed = False
letter3guessed = False
letter4guessed = False
letter5guessed = False
letter6guessed = False