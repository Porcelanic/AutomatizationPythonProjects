from pynput import keyboard
import pyautogui

# Global variable to count the number of inputs
count = 0
# Global variable to stop the listeners
end = False
record = False

class MouseInput:
    def __init__(self, typeOfInput, coordinateX, coordinateY):
        global count
        self.order = count
        count += 1
        self.typeOfInput = typeOfInput
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY

class KeyboardInput:
    def __init__(self, typeOfInput, key):
        global count
        self.order = count
        count += 1
        self.typeOfInput = typeOfInput
        self.key = key

# Create an array (list) and add the object
keyboard_array = []
mouse_array = []

# KEYBOARD FUNCTIONS
def on_press(key):
    print(f"Key {key} pressed")
    if key == '+':
        global record
        record = not record
    if record:
        keyboard_array.append(KeyboardInput("Press", key))


# This function is called every time a key is released
def on_release(key):
    print(f"Key {key} released")
    # You can stop the listener by returning False
    if key == keyboard.Key.esc:
        global end
        end = True
        # Click the mouse to stop the mouse listener
        pyautogui.click()
        return False


# MOUSE FUNCTIONS
def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")


def on_click(x, y, button, pressed):
    if end:
        return False
    elif pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
        if record:
            mouse_array.append(MouseInput("Click", x, y))
    else:
        print(f"Mouse released at ({x}, {y}) with {button}")


def on_scroll(x, y, dx, dy):
    print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")
