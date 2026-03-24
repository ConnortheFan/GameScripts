"""Record a macro for use by macro_playback.py

Only records mouse clicks, not keyboard events.
"""

from pynput import keyboard, mouse
import time
import json

events = []
start_time = None
recording = True

def on_click(x, y, button, pressed):
    events.append(("mouse_click", x, y, pressed, time.time() - start_time))

def on_press(key):
    global recording
    if key == keyboard.Key.esc:
        print("Stopping recording...")
        recording = False

def record():
    global start_time, recording
    start_time = time.time()
    mouse.Listener(on_click=on_click).start()
    keyboard.Listener(on_press=on_press).start()
    while recording:
        pass

def save(filename="macro.json"):
    with open(filename, "w") as f:
        json.dump(events, f)

if __name__ == "__main__":
    print("Recording macro. Press ESC to stop.")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Recording started.")
    record()
    save()