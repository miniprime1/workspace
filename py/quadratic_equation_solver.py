from math import *

print("Quadratic Equation Solver v1.0")
print("Copyright (c) 2021 miniprime1. All rights reserved.")
print("[Equation: ax^2 + bx + c = 0]\n")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

try:
    print("\nSolving Equation...")
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print("Done!\n")
    print("Equation:\n" + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0" + "\n")
    print("Result:\n" + "x = " + str(x1) + " or " + "x = " + str(x2))
except Exception as err:
    print("Error:", str(err))