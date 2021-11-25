import pyautogui, time
pyautogui.FAILSAFE = False

time.sleep(5)
while True:
    pyautogui.typewrite("1")
    pyautogui.press("enter")
    