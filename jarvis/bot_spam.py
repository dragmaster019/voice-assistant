import pyautogui
import time
time.sleep(2)
f = open("everyone is chutiya", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("9027737639")
