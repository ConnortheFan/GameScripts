"""Playback a macro recorded by macro_recorder.py

Only plays back mouse clicks, not keyboard events.
"""

import pyautogui
import json

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
events = []
old_time = 0.0

def load(filename="macro.json"):
    global events
    with open(filename, "r") as f:
        events = json.load(f)

def playback():
    global old_time
    for event in events:
        event_type, x, y, pressed, t = event
        pyautogui.sleep(t - old_time)
        old_time = t
        if event_type == "mouse_click":
            if pressed:
                pyautogui.mouseDown(x=x, y=y)
            else:
                pyautogui.mouseUp(x=x, y=y)

if __name__ == "__main__":
    print("Playing back macro...")
    load()
    playback()