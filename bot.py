import pyautogui
import keyboard
import win32api, win32con
import time

# Brute Force Clicking Program

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
# Run conditon
run = True
# List comprehension to assign x value positions
positions = [i for i in range(550, 1400, 100)]  
print("Running")
# Main Loop
while run:
    # Only Activate when w key is pressed
    while keyboard.is_pressed('w'):
        # Loop through all postions and click
        for item in positions:
                click(item)
    # Quit when q is pressed
    if keyboard.is_pressed('q'):
        run = False
