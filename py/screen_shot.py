import PIL, pyautogui, os

print("Screen Shot, version 1.0")
print("Copyright (c) 2020 miniprime1")
print("[Require: pyautogui, PIL]\n")

print("Options")
print("1. Screen Shot")
print("2. Install requirements")
opt = int(input("Your choice: "))

if opt == 1:
    input("\nPress enter key to generate screenshot")
    try:
        pyautogui.screenshot("screenshot.png")
        print("\nDone!")
    except:
        print("\nError!")
    
elif opt == 2:
    print("")
    os.system("pip3 install pillow")
    print("")
    os.system("pip3 install pyautogui")
    print("")
    os.system("pip install pillow")
    print("")
    os.system("pip install pyautogui")

else:
    print("\nError: invalid choice")

input("\nPress enter key to exit")