import threading
import pyautogui
from pynput import mouse
from pynput import keyboard
from . import Listeners as l

gui_wait_event = threading.Event()

def guiThread():
    while True:
        print("Waiting for GUI")
        gui_wait_event.wait()
        gui_wait_event.clear()
        main()
        

def killThreads():
    l.setKillSwitch(True)
    l.rc.startReRecord()
    current_position = pyautogui.position()
    new_position = (current_position.x + 1, current_position.y)
    pyautogui.moveTo(new_position)
    pyautogui.press('space')
    l.setKillSwitch(False)
    


# Define the function to start the keyboard listenerheloworld
def start_keyboard_listener():
    with keyboard.Listener(on_press=l.on_press, on_release=l.on_release) as listener:
        listener.join()


# Define the function to start the mouse listener
def start_mouse_listener():
    with mouse.Listener(on_click=l.on_click, on_move=l.on_move) as listener:
        listener.join()

def main():
    # Create threads for the keyboard and mouse listeners
    keyboard_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
    mouse_thread = threading.Thread(target=start_mouse_listener, daemon=True)

    # Start the keyboard listener thread
    keyboard_thread.start()

    # Start the mouse listener thread°
    mouse_thread.start()

    
    # Wait for the keyboard thread to finish
    keyboard_thread.join()
    print("Keyboard thread finished")

if __name__ == "__main__":
    l.main = True
    main()


