#!/usr/bin/env python3

"""
File: madlibs.py
Name:

A madlibs adventure!
Concepts covered: Strings, IO, printing
"""

def main():
    print("Mad Libs!")
    noun1 = input("Plural Noun;")
    adj1 = input("Adjective;")
    noun2 = input("Same Plural Noun;")
    adj2 = input("Same Adjective;")
    verb1 = input("Verb;")
    Location1 = input("Location;")
    print("I like " +str(noun1) + " they are " +str(adj1) + ". So I wrote a poem. It goes:")
    print("I like " +str(noun2) + " they are " +str(adj2) + " I like to " +str(verb1) + " them at the " +str(Location1) + ".")
    sleep(10)
if __name__ == "__main__":
    main()
