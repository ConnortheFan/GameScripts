"""Rare Enemy Finder for Your Chronicle

Find 1 rare enemy on the map set to shortcut slot 1.
Make sure to set shortcut slot 2 to any other map.
"""

from PIL import ImageGrab
import pyautogui
import pygetwindow as gw
import keyboard

def main():

    # update x and y using python -m pyautogui
    # Remember to set 1 to rare enemy area and 2 to anything else
    x = 410
    y = 410
    alive = (235, 100, 100)
    switchDelay = 0.05

    # no need to update x and y if following code is run
    win = gw.getWindowsWithTitle('YourChronicle')[0]
    win.activate()
    win.moveTo(10, 140)
    win.resizeTo(1060, 680)

    orig_x, orig_y = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.sleep(switchDelay)
    pyautogui.moveTo(orig_x, orig_y)

    pyautogui.press('2')
    pyautogui.sleep(switchDelay)
    pyautogui.press('1')
    pyautogui.sleep(switchDelay)

    counter = 0

    while(True):
        counter += 1
        # Grab enemy 2 healthbar color
        screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
        color = screenshot.getpixel((0,0))

        if keyboard.is_pressed('q'):
            print("Exiting...")
            break

        if color == alive:
            pyautogui.press('2')
            pyautogui.sleep(switchDelay)
            pyautogui.press('1')
            pyautogui.sleep(switchDelay)
        else:
            print(f"Rare enemy found after {counter} tries")
            pyautogui.sleep(5)

if __name__ == "__main__":
    main()