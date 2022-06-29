### Calculator Program ###
# CS170 - Acorn Project
# Team: Backcorner
# Members: Jackson Clarke, Noah Lloyd, Franck Sokora, and Spencer Wilson
# June 2022

### Imports ###
import math


### Variables ###
isRunning = True
runningTotal = 0

### Functions ###

# Addition
def add(x, y):
    answer = x + y
    return answer


# Subtraction
def subtract(x, y):
    total = x - y
    return total


# Multiplication
def multiply(x, y):
    total = x * y
    return total


# Division
def divide(x, y):
    total = x / y
    return total


# Area of a circle
def area_circle(radius):
    total = math.pi * radius**2
    return total


# Area of a square
def area_square(side):
    total = side**2
    return total


# Area of a rectangle
def area_rectangle(l, w, h):
    total = l * w * h
    return total


# Exponent
def exponent(x, y):
    total = x**y
    return total


# Clear
def clear():
    global runningTotal
    runningTotal = 0


# Quit
def quit():
    global isRunning
    isRunning = False


# Error
def checkError(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Error: Please enter a number.")
        return True


### Main ###
def main():
    x = float(input("Please enter first number "))
    y = float(input("Please enter the second number "))
    operator = input(
        "Please select an operator\n1 = +\n2 = -\n3 = *\n4 = /\n\
    5 = Area of a circle\n6 = Area of a square\n7 = Area of a rectangle\n8 = Exponent\n\
    9 = Clear\n10 = Quit\n"
    )
