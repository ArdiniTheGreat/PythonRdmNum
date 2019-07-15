#!/usr/bin/env python3

"""
File: dice.py
Name:

Rolls a dice and outputs the result
Concepts covered: Random, printing
"""

import random

def main():
    Again = 1
    while(Again>0):
        dice = random.randint(1,6)
        input("Press Enter to roll!")
        print("You rolled a " + str(dice))
        rollagain = (input("Again? y/n;"))
        if(rollagain == "y"):
           Again = 1
        else:
            break
if __name__ == "__main__":
    main()

