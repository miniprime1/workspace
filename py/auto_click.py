import pyautogui

def AutoClick():
    while True:
        pyautogui.click()

print("Auto Click CLI v1.0")
print("Copyright (c) 2021 miniprime1\n")

print("[ Press 'Ctrl+C' to exit ]")
input("[ Press enter key to start ]")

try: AutoClick()
except KeyboardInterrupt: pass
except Exception as err: print(f"Error: unecepted error occurred: {str(err)}")