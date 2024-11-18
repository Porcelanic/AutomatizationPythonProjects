from pynput import keyboard

# This function is called every time a key is pressed
def on_press(key):
    print(f"Key {key} pressed")

# This function is called every time a key is released
def on_release(key):
    print(f"Key {key} released")
    # You can stop the listener by returning False
    if key == keyboard.Key.esc:
        return False

# Start listening for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()