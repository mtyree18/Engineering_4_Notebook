from math import sqrt

def discriminant(a, b, c):
    d = (b * b) - 4 * a * c
    return d

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
    
x = input("Press Enter to run again, press x then Enter to quit")

while x == "":
    print("Quadratic Solver")
    print("Enter the coefficients for ax^2 + bx + c")
    a = int(input("Enter coefficient a"))
    b = int(input("Enter coefficient b"))
    c = int(input("Enter coefficient c"))
    a1 = str(a)
    b1 = str(b)
    c1 = str(c)
    xvertex = (b * -1)/(2 * a)
    yvertex = a * (xvertex * xvertex) + b * xvertex + c
    print("You entered " + a1 + "x^2 + " + b1 + "x + " + c1)
    dis = discriminant(a, b, c)
    if(findSign(dis) == ("negative")):
        print("There are no real roots")
    else:
        print("Root #1: " + str(findRoot1(a, b)))
        print("Root #2: " + str(findRoot2(a, b)))
        print(f"The vertex form is y = (x - " + {xvertex} + ")^2 + " {yvertex})
    x = input("Press Enter to run again, press x then Enter to quit")
