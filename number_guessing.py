# Number Guessing Game

import random
import time
number = random.randint(1, 200)


def intro():

    print("May I ask your name?")
    print(number)
    name = input()
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 to 200 ")
    time.sleep(0.5)
    print("Go ahead, GUESS!")


def pick():
    guesses_taken = 0
    while guesses_taken < 6:
        time.sleep(0.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)

            if guess < 200 and guess >= 1:
                guesses_taken += 1
                if guess < number:
                    print("The number you guessed is too low.")
                if guess > number:
                    print("The number you guessed is too high.")
                if guess != number:
                    time.sleep(0.5)
                    print("Please Guess again.")
                if guess == number:
                    print("Right Choice baby!")
                    break
            if guess > 200 or guess < 1:
                2
                print("Silly Goose! That number is out of range!")
                time.sleep(0.3)
                print("Please enter a number between 1 and 200 only!")
        except:
            print(f"I don't think that {guess} is a number. Sorry!")

    if guess == number:
        guesses_taken = str(guesses_taken)
        print(f"Good job mate! The number I was thinking was indeed {number}")


playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Y" or playagain == "Yes":
    number = random.randint(1, 200)
    intro()
    pick()
    print("Do you wish to play again?")
    playagain = input()
