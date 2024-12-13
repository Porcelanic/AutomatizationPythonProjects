from pynput import keyboard
import threading
import pyautogui

ESCAPE_KEY = keyboard.Key.esc
endRecording = False
mouseEnd = False

# KEYBOARD FUNCTIONS
def on_press(key):
    print(f"{key} pressed")

# This function is called every time a key is released
def on_release(key):
    global endRecording, mouseEnd
    # You can stop the listener by returning False
    if key == ESCAPE_KEY and not endRecording:
        endRecording = True
    elif key == ESCAPE_KEY and endRecording:
        return False


def on_click(x, y, button, pressed):
    if pressed:
        print(f"{button} pressed at {x}, {y}")
    else:
        print(f"{button} released at {x}, {y}")


def on_move(x, y):
    print(f"Mouse moved to {x}, {y}")
