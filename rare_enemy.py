from PIL import ImageGrab
import pyautogui
import time
import pygetwindow as gw

def main():

    # update x and y using python -m pyautogui
    # Remember to set 1 to rare enemy area and 2 to anything else
    x = 410
    y = 410
    alive = (235, 100, 100)

    # no need to update x and y if following code is run
    win = gw.getWindowsWithTitle('YourChronicle')[0]
    win.activate()
    win.moveTo(10, 140)
    win.resizeTo(1060, 680)

    orig_x, orig_y = pyautogui.position()
    pyautogui.click(x, y)
    time.sleep(1)
    pyautogui.moveTo(orig_x, orig_y)

    pyautogui.press('2')
    time.sleep(0.1)
    pyautogui.press('1')
    time.sleep(0.1)

    counter = 0

    while(True):
        counter += 1
        # Grab enemy 2 healthbar color
        screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
        color = screenshot.getpixel((0,0))

        if color == alive:
            pyautogui.press('2')
            time.sleep(0.1)
            pyautogui.press('1')
            time.sleep(0.1)
        else:
            print(f"Rare enemy found after {counter} tries")
            time.sleep(15)

if __name__ == "__main__":
    main()