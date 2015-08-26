import random

def welcome():
    print("Hi there! Let's play. You have to guess the number between 1 and 10 in 5 trys!")

def guess():
    number = random.randint(1, 10)
    for i in range(4):
        guess = input("What's the number?")
        guess = int(guess)
        if guess == number:
            print("You win!")
        elif guess > number:
            print("Guess lower!")
        elif guess < number:
            print("Guess higher!")

welcome()
guess()
