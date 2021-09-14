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
print("Sum: " + str(doMath("Sum", a, b)))
print("Div: " + str(doMath("Div", a, b)))
print("Prod: " + str(doMath("Prod", a, b)))
print("Quo: " + str(doMath("Quo", a, b)))
print("Mod: " + str(doMath("Mod", a, b)))
