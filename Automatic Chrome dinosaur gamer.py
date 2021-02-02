from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# X:  833 Y:  406 RGB: (118,  17,   1)
# >>> pyautogui.displayMousePosition()
# Press Ctrl-C to quit.
# X:  727 Y:  406 RGB: (206, 106, 118)
# >>> pyautogui.displayMousePosition()
# Press Ctrl-C to quit.
# X:  638 Y:  409 RGB: (207, 108, 118)
# >>> pyautogui.displayMousePosition()
# Press Ctrl-C to quit.
# X:  532 Y:  413 RGB: (205, 105, 118)

def Click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0, 0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(833, 400) [0] == 0:
        Click(833, 400)
    if pyautogui.pixel(727, 400) [0] == 0:
        Click(727, 400)
    if pyautogui.pixel(638, 400) [0] == 0:
        Click(638, 400)
    if pyautogui.pixel(532, 400) [0] == 0:
        Click(532, 400)