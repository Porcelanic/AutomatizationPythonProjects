import keyboard  # Detect key presses
import pyautogui  # Perform actions like clicks
import threading  # Use threads for background tasks
import time

KeepGoing = True  # Main loop condition
pyautogui.PAUSE = 0

# Using threading.Event() for better thread control
auto_click_event = threading.Event()

def AutoClicker():
    while KeepGoing:
        auto_click_event.wait()  # Wait until auto-clicking is allowed
        pyautogui.mouseDown()  # Perform click
        time.sleep(0.01)  # Click duration
        pyautogui.mouseUp()
        time.sleep(0.01)  # Interval between clicks

def changeState(state):
    if state:
        auto_click_event.set()  # Start auto-clicking
    else:
        auto_click_event.clear()  # Stop auto-clicking

# Start the background autoclicker threadx
thread = threading.Thread(target=AutoClicker, daemon=True)
thread.start()

while KeepGoing:
    key = keyboard.read_event()  # Detect key press (non-blocking)
    if key.event_type == keyboard.KEY_DOWN:  # Only react to key press events
        if key.name == 'c':  # Start clicking
            print("You pressed the 'c' key")
            changeState(True)
        elif key.name == 'v':  # Stop clicking
            print("You pressed the 'v' key")
            changeState(False)
        elif key.name == 'x':  # Exit the program
            print("You pressed the 'x' key")
            KeepGoing = False
            changeState(False)  # Stop clicking before exiting