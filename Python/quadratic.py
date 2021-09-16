# Python Program 02 - Quadratic Solver (ENGR4)

#Written by Max Tyree

#9.16.2021

from math import sqrt

print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c")
a = int(input("Enter coefficient a"))
b = int(input("Enter coefficient b"))
c = int(input("Enter coefficient a"))

def discriminant(a, b, c):
    d = (b * b) - 4 * a * c
    return d
    
dis = discriminant(a, b, c)

def findRoot1(a, b):
    r1 = (-b + dis) / (2 * a)
    return r1

def findRoot2(a, b):
    r2 = (-b - dis)/(2 * a)
    return r2
    
def findSign(dis):
    if(dis < 0):
        s = ("negative")
    else:
        s = ("positive")
    return s
if(findSign(dis) == ("negative")):
    print("There are no real roots")
else:
    print("Root #1: " + str(findRoot1(a, b)))
    print("Root #2: " + str(findRoot2(a, b)))
x = input("Press Enter to run again, press x then Enter to quit")
while x == "":
    print("Quadratic Solver")
    print("Enter the coefficients for ax^2 + bx + c")
    a = int(input("Enter coefficient a"))
    b = int(input("Enter coefficient b"))
    c = int(input("Enter coefficient a"))
    if(findSign(dis) == ("negative")):
        print("There are no real roots")
    else:
        print("Root #1: " + str(findRoot1(a, b)))
        print("Root #2: " + str(findRoot2(a, b)))
    x = input("Press Enter to run again, press x then Enter to quit")
