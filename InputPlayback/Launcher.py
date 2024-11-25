import threading
from pynput import mouse
from pynput import keyboard
import Listeners as l

test = 0


# Define the function to start the keyboard listenerheloworld
def start_keyboard_listener():
    with keyboard.Listener(on_press=l.on_press, on_release=l.on_release) as listener:
        listener.join()


# Define the function to start the mouse listener
def start_mouse_listener():
    with mouse.Listener(on_click=l.on_click, on_move=l.on_move) as listener:
        listener.join()


# Create threads for the keyboard and mouse listeners
keyboard_thread = threading.Thread(target=start_keyboard_listener)
mouse_thread = threading.Thread(target=start_mouse_listener, daemon=True)

# Start the keyboard listener thread
keyboard_thread.start()

# Start the mouse listener thread°
mouse_thread.start()

# Wait for both threads to finish
keyboard_thread.join()
