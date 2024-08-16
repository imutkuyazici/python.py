import pyautogui
import time

time.sleep(10)

def mesah():
    pyautogui.write("Berkay Abi")
    pyautogui.press("enter")

while True:
    mesah()
    time.sleep(0)
