import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} : "))  
        if guess > random_number:
            print("Too high...")
        elif guess < random_number:
            print("Too low...")

    print("good job")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f"guess num  if {guess} high press h else press l :")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("good job")
computer_guess(10)