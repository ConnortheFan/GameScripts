"""Playback a macro recorded by macro_recorder.py

Only plays back mouse clicks, not keyboard events.
"""

import pyautogui
import json

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
events = []

def load(filename="macro.json"):
    global events
    with open(filename, "r") as f:
        events = json.load(f)

def playback():
    for event in events:
        event_type, x, y, pressed, delay = event
        pyautogui.sleep(delay)
        if event_type == "mouse_click":
            if pressed:
                pyautogui.mouseDown(x=x, y=y)
            else:
                pyautogui.mouseUp(x=x, y=y)

if __name__ == "__main__":
    print("Playing back macro...")
    load()
    playback()