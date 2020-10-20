import random

def generateRandomNumbers (min: int, max: int):
    return random.randint(min, max)

def isEven (number: int):
    return number % 2 == 0

def factorial (number: int):
    if number == 1: 
        return 1
    else:
        return number * factorial(number - 1)

def capitalizeFormat (string: str):
    return string.capitalize()

def prueba(number):
    if (isEven(number)):
        return number * 2
    else:
        return number * 5
