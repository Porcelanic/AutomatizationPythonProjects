import keyboard  # Detect key presses
import pyautogui  # Perform actions like clicks
import threading  # Use threads for background tasks
import time

KeepGoing = True  # Main loop condition
pyautogui.PAUSE = 0

# Using threading.Event() for better thread control
auto_click_event = threading.Event()
gui_wait_event = threading.Event()

# The delays performed here are to ensure that any program recognices the clicks
# If there are NO delays, some programs may not detect the clicks
def AutoClicker():
    while KeepGoing:
        auto_click_event.wait()  # Wait until auto-clicking is allowed
        pyautogui.mouseDown()  # Perform click
        time.sleep(0.01)  # Click duration
        pyautogui.mouseUp() # Release click
        time.sleep(0.01)  # Delay between clicks

def changeState(state):
    if state:
        auto_click_event.set()  # Start auto-clicking
    else:
        auto_click_event.clear()  # Stop auto-clicking

#Controls the Autoclicker according to the GUI
def enableAutoClicker(enable):
    if enable:
        gui_wait_event.set()
    else:
        changeState(enable)
        gui_wait_event.clear()

def main():
    global KeepGoing
    # Start the background autoclicker thread
    thread = threading.Thread(target=AutoClicker, daemon=True)
    thread.start()
    while KeepGoing:
        gui_wait_event.wait()  # Wait until the GUI allows the autoclicker to run
        key = keyboard.read_event()  # when the gui_wait_event is cleared,the program may continue because it's stucked here
        if key.event_type == keyboard.KEY_DOWN and gui_wait_event.is_set(): # this condition is to avoid the autoclicker to start when the GUI is not ready
            if key.name == 'c':  # Start clicking
                print("You pressed the 'c' key")
                changeState(True)
            elif key.name == 'v':  # Stop clicking
                print("You pressed the 'v' key")
                changeState(False)
            elif key.name == 'x' and __name__ == "__main__":  # Exit the program
                print("You pressed the 'x' key")
                KeepGoing = False
                changeState(False)  # Stop clicking before exiting

if __name__ == "__main__":
    gui_wait_event.set()
    main()