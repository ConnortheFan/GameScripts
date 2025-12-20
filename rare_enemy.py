from PIL import ImageGrab
import pyautogui
import time
import pygetwindow as gw

def main():

    # update x and y using python -m pyautogui
    x = 451
    y = 341
    alive = (235, 100, 100)

    orig_x, orig_y = pyautogui.position()
    pyautogui.click(x, y)
    time.sleep(1)
    pyautogui.moveTo(orig_x, orig_y)

    pyautogui.press('2')
    time.sleep(0.1)
    pyautogui.press('1')
    time.sleep(0.1)

    while(True):
        # Grab enemy 2 healthbar color
        screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
        color = screenshot.getpixel((0,0))

        if color == alive:
            pyautogui.press('2')
            time.sleep(0.1)
            pyautogui.press('1')
            time.sleep(0.1)
        else:
            print("Rare enemy")
            time.sleep(15)

if __name__ == "__main__":
    main()