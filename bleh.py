import pyautogui
import time
time.sleep(5)
f = open("file.txt")
z = f.readlines()
for x in z:
    pyautogui.typewrite(x)
    pyautogui.press("enter")
    time.sleep(1)
