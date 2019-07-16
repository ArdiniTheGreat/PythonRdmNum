import random

def main():
   randomnumber = random.randint(1,100)
   Correct = 1
   while(Correct>0):
      guess = int(input("Try to guess the number;"))
      if (guess>randomnumber+30 and guess<randomnumber+50):
         print("Your guess is a lot higher than the number.")
      if (guess<randomnumber-30 and guess>randomnumber-50):
         print("Your guess is a lot lower than the number.")
      if (guess>randomnumber+9 and guess<randomnumber+29):
         print("Your guess is higher than the number.")
      if (guess<randomnumber-9 and guess>randomnumber-29):
         print("Your guess is lower than the number.")
      if (guess>randomnumber and guess<randomnumber+10):
         print("Your guess is slightly higher than the number.")
      if (guess<randomnumber and guess>randomnumber-10):
         print("Your guess is slightly lower than the number.")
      if (guess==randomnumber):
         print("You guessed the number!")
         break
if __name__ == "__main__":
    main()