import platform
import os

def clear():
    windows = (platform.system() == "Windows")
    if windows: os.system("cls")
    else: os.system("clear")

if __name__ == "__main__":
    clear()