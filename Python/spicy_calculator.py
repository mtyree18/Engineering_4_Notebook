# Python Program 01 - Spicy Calculator (ENGR4)

#Written by Max Tyree

#9.14.2021

a = int(input("Enter a number"))
b = int(input("Enter a second number"))
def doMath(operand, a, b): #establishing the function
    if operand == "Sum": #giving criteria for the function and returning the value based on that criteria
        return a + b
    if operand == "Div":
        return a / b
    if operand == "Prod":
        return a * b
    if operand == "Quo":
        return a / b
    if operand == "Mod":
        return a % b
#made a for loop that goes from 1 to the value entered + 1 so that it goes 
#all the way to the number. Then I multiplied 1 times the next number in the sequence
#over and over, redefining the varialbe that was originally 1 to equal what it just got multiplied to
    if operand == "Fact1":
        fact = 1
        for i in range(1,a+1):
            fact = fact * i
        return fact
    if operand == "Fact2":
        fact = 1
        for i in range(1,b+1):
            fact = fact * i
        return fact
#prints the doMath function as a string so that it can concatenate with the string that displays the current operand
print("Sum: " + str(doMath("Sum", a, b)))
print("Div: " + str(doMath("Div", a, b)))
print("Prod: " + str(doMath("Prod", a, b)))
print("Quo: " + str(doMath("Quo", a, b)))
print("Mod: " + str(doMath("Mod", a, b)))
print("Fact1: " + str(doMath("Fact1", a, b)))
print("Fact2: " + str(doMath("Fact2", a, b)))
