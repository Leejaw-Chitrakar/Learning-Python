import pyautogui
import time

print("Writing after 3 secounds!!")
time.sleep(3)
for i in range(5):
    for j in range(5):
        pyautogui.typewrite("YUP!!  ")
    pyautogui.press("enter")

print("Done!!")
