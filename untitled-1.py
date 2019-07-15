import random

def main():
    randnum = random.randint(1,10)
    tries=5
    while(tries>0):
        guess = int(input("Pick a number between 1 and 10;"))
        if (guess == randnum):
            print("You Win!")
            break
        else:
            print("Wrong.")
            tries = tries - 1
            if(tries==0):
                print("You have no tries left")
            else:
                print("You have " + str(tries) + " tries left.")
        if(tries==0):
            print("You're a faliure")
if __name__ == "__main__":
    main()