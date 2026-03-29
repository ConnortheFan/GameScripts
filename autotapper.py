"""Simulates hundreds of taps per second for the game Bongo Cat

For the new achievements of 25 million taps.
"""

from pynput import keyboard
import pyautogui
import time

pyautogui.PAUSE = 0

keys = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'down', 'left', 'right', 'up', 'shiftleft', 'shiftright', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'space']

tapping = True
tapsPerSec = len(keys) * 5

def on_press(key):
    global tapping
    if key == keyboard.Key.esc:
        print("Stopping tapping...")
        tapping = False

def tap(n=1):
    for i in range(n):
        for key in keys:
            pyautogui.keyDown(key)
            time.sleep(1/tapsPerSec)
        for key in keys:
            pyautogui.keyUp(key)
        time.sleep(1/20)

keyboard.Listener(on_press=on_press).start()

print(f"Going at ~{tapsPerSec} keys per second")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Started")
while tapping:
    tap()
