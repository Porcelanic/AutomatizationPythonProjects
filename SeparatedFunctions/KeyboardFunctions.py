from pynput import keyboard
def on_press(key):
    print(f"Key {key} pressed")

# This function is called every time a key is released
def on_release(key):
    print(f"Key {key} released")
    # You can stop the listener by returning False
    if key == keyboard.Key.esc:
        return False