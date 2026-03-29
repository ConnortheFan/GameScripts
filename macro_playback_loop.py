"""Play the macro from macro_record.py in an infinite loop

Press ESC to stop the infinite playback.
"""

import macro_playback
from pynput import keyboard
import pyautogui

macro_playback.playing = True

def on_press(key):
    if key == keyboard.Key.esc:
        print("Stopping playback...")
        macro_playback.playing = False

if __name__ == "__main__":
    keyboard.Listener(on_press=on_press).start()

    print("Playing back macro in an infinite loop, press ESC to exit")
    macro_playback.load()
    print("3...")
    pyautogui.sleep(1)
    print("2...")
    pyautogui.sleep(1)
    print("1...")
    pyautogui.sleep(1)
    print("Playback started.")
    while macro_playback.playing:
        macro_playback.playback()