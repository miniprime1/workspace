import os

print("C Interpreter v1.0 (Require 'Clang')")
print("Copyright (c) 2020 miniprime1. All rights reserved.")
print("[Enter 'RUN' to Run the Code]")

while True:
    f = open("stdin.c", 'w')
    # f = open("stdin.cpp", 'w')
    try: 
        stdin = input("\n>>> ")
    except:
        f.close()
        os.remove("stdin.c")
        break
    f.write(stdin + '\n')
    while True:
        stdin = input("... ")
        if stdin == "RUN": break
        f.write(stdin + '\n')
    f.close()
    os.system("clang stdin.c")
    os.system("./a.out")
    os.remove("stdin.c")
    os.remove("a.out")