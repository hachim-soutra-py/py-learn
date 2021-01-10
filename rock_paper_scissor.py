import random


def play():
    user = input("what your choise ??? r for rock ,s for scissor ,p for papper")
    computer = random.choice(['r','p','s'])

    if user