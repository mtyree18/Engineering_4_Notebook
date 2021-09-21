# Python Program 02 - Quadratic Solver (ENGR4)

#Written by Max Tyree

#9.16.2021

from math import sqrt #importing the necessary math elements

def discriminant(a, b, c): #This function finds the discriminant of the quadratic
    d = (b * b) - 4 * a * c 
    return d

def findRoot1(a, b): #This function finds the root that relies on a positive discriminant
    r1 = (-b + dis) / (2 * a)
    return r1

def findRoot2(a, b): #This function finds the root that relies on a negative discriminant
    r2 = (-b - dis)/(2 * a)
    return r2
    
def findSign(dis): #This function figures out if the function is positive or negative. This is used to figure out if there are real roots or not
    if(dis < 0):
        s = ("negative")
    else:
        s = ("positive")
    return s
    
x = input("Press Enter to run again, press x then Enter to quit") #This is the first message that appears, and it tells you how to operate the program

while x == "": #This while loop relies on you pressing enter, so that when you enter anything other than enter the loop stops and the program ends
    print("Quadratic Solver") #These print statements introduce the program
    print("Enter the coefficients for ax^2 + bx + c")
    a = int(input("Enter coefficient a")) #These variables are gathered by you typing in a string, which I then had to convert to an integer to use mathmatically
    b = int(input("Enter coefficient b"))
    c = int(input("Enter coefficient c"))
    a1 = str(a) #These variables are the string versions of the variables that were just entered
    b1 = str(b)
    c1 = str(c)
    xvertex = (b * -1)/(2 * a) #This is an algorithm to find the x value of the vertex, which I will need for the vertex formula
    yvertex = a * (xvertex * xvertex) + b * xvertex + c #This is an algorithm to find the y value of the vertex, which I will need for the vertex formula
    print("You entered " + a1 + "x^2 + " + b1 + "x + " + c1) #This statement is part of the spicy part, and just shows you the equation that gets made based off what you entered
    dis = discriminant(a, b, c) #I made this variable because I didn't want to type discriminant(a, b, c) everytime
    if(findSign(dis) == ("negative")): #This if statement puts all the parts together. It checks if findSign returned positive or negative, and if it's negative it prints there are no real roots
        print("There are no real roots")
    else: #This part will run if the discriminant is positive because the negative option has already been run if it exists. It then prints what findRoot 1 and 2 returns
        print("Root #1: " + str(findRoot1(a, b))) #These prints statements print the roots
        print("Root #2: " + str(findRoot2(a, b)))
        print(f"The vertex form is y = (x-{xvertex})^2+{yvertex}") #This prints the vertex form based on what you entered
    x = input("Press Enter to run again, press x then Enter to quit") #This is at the end because we need to reestablish x to figure out if you want to run the program again or not
