# Import Require Packages
from math import *
from sympy.solvers import solve
from sympy import Symbol, Eq
from sys import exit

# Pre-defined Valuable
eq_list = []
cmd_list = []
sol = 0
key = 0

# Info
print("Equation Solver v1.0")
print("Copyright (c) 2020 miniprime1\n")

# Number of Symbol
rang1 = int(input("Enter Number of Symbol (max=26): "))
if 1 <= rang1 <= 26:
  for i in range(rang1):
    exec("".join((str(chr(97+i)), str("="), str("Symbol('") + str(chr(97+i)) + str("')"))))
else:
  rang1 = 1
  a = Symbol('a')

# Number of Equation
rang2 = int(input("Enter Number of Equation (max=26): "))
print()

# Print Usable Symbol
print("Usable Symbol:", end=" ")
if rang1 == 1:
  print(chr(97))
else:
  for i in range(rang1-1):
    print(chr(97+i), end=', ')
  print(chr(97+(i+1)))

# Make Symbol Tuple
sym_list = "("
if rang1 == 1:
  print(chr(97))
else:
  for i in range(rang1-1):
    sym_list += chr(97+i)
    sym_list += ','
  sym_list += chr(97+(i+1))
sym_list += ')'
  
# Get and Clean Equation
print()
if 1 <= rang2 <= 26:
  cmd2 = '['
  for i in range(0, rang2): 
    tmp = input(f"Enter Equation {i+1}: ")
    try:
      eq1, eq2 = tmp.split("=")
      cmd_list.append("Eq(" + eq1 + "," + eq2 + ")")
      eq_list.append(tmp)
    except:
      cmd_list.append("Eq(" + tmp + "," + 0 + ")")
      eq_list.append(tmp + '=' + '0')
  for i in range(0, rang2): 
    cmd2 += str(cmd_list[i])
    if i == rang2-1: pass
    else: cmd2 += ', '
  cmd2 += ']'
else:
  rang2 = 1
  cmd2 = 'a'

# Solving Equation
if rang2 == 1: 
  cmd_result = "".join((str('sol'), str('='), str('solve') + str(cmd2)))
  try: 
    tmp_tuple2 = str('sol'), str('='), str('solve') + str(cmd2)
    cmd_result = "".join(tmp_tuple2)
    exec(str(cmd_result))
  except Exception as e: 
    print("\nError!\n" + str(e))
    exit()
else: 
  try: 
    tmp_tuple2 = str('sol'), str('='), str('solve') + str('(') + str(cmd2) + str(', ') + str(sym_list) + str(')')
    cmd_result = "".join(tmp_tuple2)
    exec(str(cmd_result))
  except Exception as e: 
    print("\nError!\n" + str(e))
    exit()

# Print Equations
print("\nEquation:")
for i in range(0, rang2): 
  print(str(eq_list[i]))

# Print Value (Result)
print("\nValue:")
if rang1 == 1:
  print(f"{chr(97+i)} = {sol[0]}")
else:
  if len(sol)==1:
    for i in range(rang1):
      exec("".join(("key", '=', "sol[" + chr(97+i) + "]")))
      print(chr(97+i), '=', key)
    print()
  else:
    try:
      for i in range(rang1):
        exec("".join(("key", '=', "sol[" + chr(97+i) + "]")))
        print(chr(97+i), '=', key)
      print()
    except:
      for i in range(len(sol)):
        for j in range(rang1):
          print(chr(97+j), '=', sol[i][j], end=", ")
        print()