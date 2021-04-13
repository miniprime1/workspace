from sympy.parsing.sympy_parser import *
from sympy import *
from math import *

print("Integral Calculator v1.0")
print("Copyright (c) 2021 miniprime1\n")

variable = input("Enter Symbol: ")
x = symbols(variable)

expr = input("Enter Expression: ")
expr = parse_expr(expr.replace("^", "**"))

upper = input("Enter Upper Bound: ")
lower = input("Enter Lower Bound: ")
non = bool(upper=="" or lower=="" or upper=="oo" or lower=="oo" or upper=="-oo" or lower=="-oo")

if non: result = integrate(expr, x)
else: result = integrate(expr, (x, lower, upper))

print("\nResult:", str(result).replace("**", "^"))