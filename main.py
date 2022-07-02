### Calculator Program ###
# CS170 - Acorn Project
# Team: Backcorner
# Members: Jackson Clarke, Noah Lloyd, Franck Sokora, and Spencer Wilson
# June 2022
# Total time: 10 hours

### Imports ###
import math


### Variables ###
isRunning = True
listOfTotals = []


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


# Clear
def clear():
    global listOfTotals
    listOfTotals = []


# Quit
def quit():
    global isRunning
    isRunning = False


# Error
def checkError(x, y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Error: Please enter a number.")
        return True


### Main ###
print("\nWelcome to the python calculator!\n")
while isRunning == True:
    if len(listOfTotals) < 1:
        x = float(input("Please enter first number: "))
        operator = int(
            input(
                "Please select an operator\n1 = +\n2 = -\n3 = *\n4 = /\n\
9 = Clear\n0 = Quit\n\nOperator Number: "
            )
        )
        y = float(input("Please enter the second number: "))

        if operator == 1:
            answer = add(x, y)
            print(answer)
            listOfTotals.append(answer)

        elif operator == 2:
            answer = subtract(x, y)
            print(answer)
            listOfTotals.append(answer)

        elif operator == 3:
            answer = multiply(x, y)
            print(answer)
            listOfTotals.append(answer)

        elif operator == 4:
            answer = divide(x, y)
            print(answer)
            listOfTotals.append(answer)

        elif operator == 9:
            clear()
            print("Cleared")

        elif operator == 0:
            quit()

        else:
            print("Error: Please enter a number.")
    else:
        counter = len(listOfTotals) - 1
        x = listOfTotals[counter]
        operator = int(
            input(
                "\nPlease select an operator\n1 = +\n2 = -\n3 = *\n4 = /\n\
9 = Clear\n0 = Quit\n\nOperator Number: "
            )
        )

        if operator == 9:
            clear()
            print("Cleared")
        elif operator == 0:
            quit()
        else:
            y = float(input("Please enter the second number: "))

            if operator == 1:
                answer = add(x, y)
                print(answer)
                listOfTotals.append(answer)

            elif operator == 2:
                answer = subtract(x, y)
                print(answer)
                listOfTotals.append(answer)

            elif operator == 3:
                answer = multiply(x, y)
                print(answer)
                listOfTotals.append(answer)

            elif operator == 4:
                answer = divide(x, y)
                print(answer)
                listOfTotals.append(answer)

            elif operator == 9:
                clear()
                print("Cleared")

            elif operator == 0:
                quit()

            else:
                print("Error: Please try again.")
# End of while loop

print("Thanks for using our python calculator!")
