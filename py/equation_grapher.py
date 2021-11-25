from sympy import symbols
from sympy.plotting import plot

x = symbols('x')
y = symbols('y')

print("Equation Grapher v1.0")
print("Copyright (c) 2020 miniprime1")
print("[Variables: (x or y)]\n")

eq = input('Enter Equation: ')
print()

try: 
    plot(eq)
except Exception as e: 
    print("Error!\n" + str(e))