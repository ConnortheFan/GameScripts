"""Play the macro from macro_record.py in an infinite loop

Press ESC to stop the infinite playback.
"""

from macro_playback import load, playback
from pynput import keyboard

playing = True

def on_press(key):
    global playing
    if key == keyboard.Key.esc:
        print("Stopping recording...")
        playing = False

if __name__ == "__main__":
    keyboard.Listener(on_press=on_press).start()

    print("Playing back macro in an infinite loop, press ESC to exit")
    load()
    while playing:
        playback()