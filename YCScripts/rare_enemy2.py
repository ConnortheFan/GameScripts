"""Rare Enemy Finder 2 for Your Chronicle

Find 2 rare enemies on the maps set to shortcut slots 1 and 2.
"""

from PIL import ImageGrab
import pyautogui
import pygetwindow as gw
from pynput import keyboard

def on_press(key):
    global stop_flag
    if key == keyboard.Key.esc:
        print("Exiting...")
        stop_flag = True

def main():
    global stop_flag
    stop_flag = False
    keyboard.Listener(on_press=on_press).start()

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
        if stop_flag:
            break

        counter += 1
        # Grab enemy 2 healthbar color
        screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
        color = screenshot.getpixel((0,0))

        if color == alive:
            pyautogui.press('2')
            pyautogui.sleep(switchDelay)
        else:
            print(f"Rare enemy 1 found after {counter} tries")
            pyautogui.sleep(5)

        if stop_flag:
            break

        screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
        color = screenshot.getpixel((0,0))

        if color == alive:
            pyautogui.press('1')
            pyautogui.sleep(switchDelay)
        else:
            print(f"Rare enemy 2 found after {counter} tries")
            pyautogui.sleep(5)

if __name__ == "__main__":
    main()