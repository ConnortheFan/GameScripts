"""Playback a macro recorded by macro_recorder.py

Plays back mouse and keyboard inputs.
"""

import pyautogui
import json
from pynput import keyboard

pyautogui.PAUSE = 0
events = []

playing = True

def on_press(key):
    global playing
    if key == keyboard.Key.esc:
        print("Stopping playback...")
        playing = False

def load(filename="macro.json"):
    global events
    with open(filename, "r") as f:
        events = json.load(f)

def playback():
    for event in events:
        if not playing:
            return

        # item = [key/button, x, y, pressed]
        event_type, delay, *item = event
        pyautogui.sleep(delay)

        if not playing:
            return
        
        if event_type == "mouse":
            if item[3]:
                pyautogui.mouseDown(x=item[1], y=item[2], button=item[0])
            else:
                pyautogui.mouseUp(x=item[1], y=item[2], button=item[0])
        elif event_type == "press":
            pyautogui.keyDown(key=item[0])
        elif event_type == "release":
            pyautogui.keyUp(item[0])

if __name__ == "__main__":
    load()
    print("Playing back macro, press ESC to exit")
    keyboard.Listener(on_press=on_press).start()
    print("3...")
    pyautogui.sleep(1)
    print("2...")
    pyautogui.sleep(1)
    print("1...")
    pyautogui.sleep(1)
    print("Playback started.")
    playback()