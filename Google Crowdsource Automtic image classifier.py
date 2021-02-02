from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import random

# X: 1231 Y:  366 RGB: (232, 240, 253)
# X:   82 Y:  725 RGB: ( 84, 141, 244)
# 1185 Y:  464 RGB: (187, 175, 161)
while True:
    
    if pyautogui.pixel(1231, 366)[0] == 232:
        pyautogui.click(82, 725)
        pyautogui.click(1185, 464)

    # # if pyautogui.pixel(1289, 449)[0] == 0:
    # #     pyautogui.click(34, 62)
    # #     time.sleep(7)
    # #     pyautogui.click(34, 62)
    # #     time.sleep(2)
    # #     pyautogui.click(34, 62)
    else:
        
        pyautogui.click(1310, 716)
        time.sleep(1)
        pyautogui.click(1310, 716)
        time.sleep(1)
        pyautogui.click(1310, 716)
        time.sleep(1)
        pyautogui.click(1310, 716)
        time.sleep(1)
        pyautogui.click(1310, 716)
        time.sleep(1)
        pyautogui.click(1310, 716)
        time.sleep(1)
        pyautogui.click(1189, 720)
        time.sleep(1)
 
    