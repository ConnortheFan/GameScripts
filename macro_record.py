"""Record a macro for use by macro_playback.py

Records mouse and keyboard inputs.
"""

from pynput import keyboard, mouse
import time
import json

events = []
last_time = None
recording = True

def on_click(x, y, button, pressed):
    global last_time
    events.append(["mouse", time.time() - last_time, str(button), x, y, pressed])
    last_time = time.time()

def on_press(key):
    global last_time, recording
    if key == keyboard.Key.esc:
        print("Stopping recording...")
        recording = False
    else:
        events.append(["press", time.time() - last_time, str(key)])
        last_time = time.time()

def on_release(key):
    global last_time
    if key != keyboard.Key.esc:
        events.append(["release", time.time() - last_time, str(key)])
        last_time = time.time()

def record():
    global last_time, last_time, recording
    last_time = time.time()
    mouse.Listener(on_click=on_click).start()
    keyboard.Listener(on_press=on_press, on_release=on_release).start()
    while recording:
        pass

def filter_events():
    global events
    filtered_events = []
    for event in events:
        item = event[2]
        # "'a'" -> "a"
        if item[0] == "'":
            event[2] = item[1]
        # "\"'\"" -> "'"
        elif item[0] == "\"":
            event[2] = "'"
        # "Button.left" -> "left"
        elif item[0] == "B":
            event[2] = item[7:]
        # "Key.space" -> "space"
        elif item[0] == "K":
            event[2] = item[4:]
        filtered_events.append(event)
    return filtered_events

def save(filename="macro.json"):
    with open(filename, "w") as f:
        json.dump(filter_events(), f)

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