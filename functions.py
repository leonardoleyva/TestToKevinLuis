import random

def generateRandomNumbers(min: int, max: int):
    return random.randint(min, max)

def isEven(number: int):
    return number % 2 == 0

def factorial(number = int):
    if number == 1: 
        return 1
    else:
        return number * factorial(number - 1)

def getlenghtString(Name: str):
    return len(Name)

print(getlenghtString("Luis"))