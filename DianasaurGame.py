from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# X:  495 Y:  301 RGB: (255, 255, 255)

# X:  817 Y:  301 RGB: ( 83,  83,  83)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(495, 301) [0] == 83:
        pyautogui.press('space')
    elif pyautogui.pixel(471, 280) [0] == 84:
        pyautogui.press('space')



    # if pyautogui.pixel(727, 400) [0] == 0:
    #     Click(727, 400)
    # if pyautogui.pixel(638, 400) [0] == 0:
    #     Click(638, 400)
    # if pyautogui.pixel(532, 400) [0] == 0:
    #     Click(532, 400)