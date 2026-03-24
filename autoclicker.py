"""This is an autoclicker script

Press ` to activate/deactivate the autoclicker
Press ESC to quit the script
Scroll up to increase CPS, scroll down to decrease CPS
"""

import pyautogui
from pynput import mouse
from pynput import keyboard

pyautogui.PAUSE = 0

cps = 20 # Clicks per second, adjust as needed

sleepTime = 1/cps
autoclickerOn = False
pressed = False
quit = False

def on_press(key):
    global pressed, autoclickerOn, quit
    if key == keyboard.KeyCode.from_char('`') and not pressed:
        pressed = True
        autoclickerOn = not autoclickerOn
        print(f"Autoclicker On: {autoclickerOn}")
    elif key == keyboard.Key.esc:
        quit = True
        print("Quitting autoclicker.")

def on_release(key):
    global pressed
    if key == keyboard.KeyCode.from_char('`'):
        pressed = False

def on_scroll(x, y, dx, dy):
    global cps, sleepTime, autoclickerOn
    if dy > 0:  # Scroll up
        cps += 1
    elif dy < 0:  # Scroll down
        cps = max(0, cps - 1)  # Prevent cps from going below 0
    if cps == 0:
        sleepTime = 1
        autoclickerOn = False
    else:
        sleepTime = 1 / cps
    print(f"Current CPS: {cps}")

def main():
    print("Running autoclicker. Press ` to toggle on/off, scroll to adjust CPS, and ESC to quit.")

    mouse.Listener(on_scroll=on_scroll).start()
    keyboard.Listener(on_press=on_press, on_release=on_release).start()

    while True:
        if autoclickerOn:
            pyautogui.mouseDown()
            pyautogui.sleep(0.0001)
            pyautogui.mouseUp()
            pyautogui.sleep(sleepTime)
        if quit:
            break

if __name__ == "__main__":
    main()