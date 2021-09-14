# Python Program 01 - Spicy Calculator (ENGR4)

#Written by Max Tyree

#9.14.2021

a = int(input("Enter a number"))
b = int(input("Enter a second number"))
def doMath(operand, a, b):
    if operand == "Sum":
        return a + b
    if operand == "Div":
        return a / b
    if operand == "Prod":
        return a * b
    if operand == "Quo":
        return a / b
    if operand == "Mod":
        return a % b
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
print("Sum: " + str(doMath("Sum", a, b)))
print("Div: " + str(doMath("Div", a, b)))
print("Prod: " + str(doMath("Prod", a, b)))
print("Quo: " + str(doMath("Quo", a, b)))
print("Mod: " + str(doMath("Mod", a, b)))
print("Fact1: " + str(doMath("Fact1", a, b)))
print("Fact2: " + str(doMath("Fact2", a, b)))
