import win32api, win32con
from pyautogui import *
import pyautogui
import time
import keyboard

# Detects a specific object and clicks that object

# Hard mode changes where we need to click depending on how fast the tiles move
HARD_MODE = False

# Controls the clicker
global auto
auto = False

# Clicking different x values, but a static y
def click(x, y=450):
    # Move Cursor
    win32api.SetCursorPos((x, y))
    # Left click down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # If we click to fast, some clicks do not register
    time.sleep(0.01)
    # Let click up
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Turns on and off the clicker
def auto_run():
    global auto
    auto = not auto

# Run condition
run = True
print("Running...")

# Main Loop
while run:
    # Stops program from breaking when image is not on screen
    pyautogui.useImageNotFoundException()
    try:
        # Loads the image we are searching for. Loads the region to scan for.
        # Confidience allows the image to not be a pixel perfect match. 0.7 = 70% match
        location = pyautogui.locateOnScreen("square.png", grayscale= True, region=(450,250,1000,500), confidence= 0.7)
        # When holding auto is true, start searching and clicking
        if auto:
            # Hardmode refers to the tile game, where tiles move faster
            if HARD_MODE:
                # Since tiles move faster, we need to place the y further down to compensate
                click(location.left+60, location.top+180)
            else:
                # If hard mode is off, we can click in the center of the tile
                click(location.left+60, location.top+80)
    except pyautogui.ImageNotFoundException:
        pass
    
    # Used to toggle the auto variable to true or false
    keyboard.add_hotkey('m', auto_run)

    
    # Quit if q is pressed
    if keyboard.is_pressed('q'):
        run = False
