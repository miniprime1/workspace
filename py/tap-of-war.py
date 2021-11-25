# *************************************** #
# Tap of War v1.0                         #
# Copyright (c) 2020 miniprime1           #
#                                         #
# Description: Simple CLI Casual Game     #
# License: MIT License (miniprime1, 2021) #
# Language: Python                        #
# Interpreter: Python 3.7.8 (win32)       #
# OS: Windows, [Untested: Unix]           #
# *************************************** #

import os
import platform
import sys

system = platform.system()
difficult = 30
index_o = int(difficult/2)
index_x = int(difficult/2)
clear = "clear"

if system == "Windows":
    import msvcrt
    clear = "cls"
else:
    import termios, tty
    clear = "clear"

def update(o, x):
    os.system(clear)
    print('[ ' + 'O '*o + 'X '*x + ']')

def check(o, x):
    if o == 0:
        return 'x'
    elif x == 0:
        return 'o'

def _getch():
    if system == "Windows":
        ch = msvcrt.getch()
        return ch.decode("utf-8")
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

print("Tap of War v1.0")
print("Copyright (c) 2020 miniprime1\n")
# print("[Recommended OS: Windows]")

print("Game Rule")
print("1. Choose a team with your friend (X or O)")
print("2. Press enter key to start the game (enter)")
print("2. Type your team's markers as fast as you can ('o' or 'x')")
print("3. If all the spaces are your team's markers, you win\n")

input("Press enter key to start ")
update(index_o, index_x)

while True:
    if _getch() == 'o':
        index_o = index_o + 1
        index_x = index_x - 1
    elif _getch() == 'x':
        index_o = index_o - 1
        index_x = index_x + 1

    update(index_o, index_x)

    if check(index_o, index_x) == 'o':
        print("\nO is winner!")
        break
    elif check(index_o, index_x) == 'x':
        print("\nX is winner!")
        break