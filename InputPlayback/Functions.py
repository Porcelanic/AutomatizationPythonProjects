from pynput import keyboard
import threading
import pyautogui
import time
import Playback as pb
# Global variable to count the number of inputs
count = 0
# Global variable to stop the listeners
endRecording = False
record = False
mouseEnd = False
recordTime = time.time()
recordKey = '|'
reRecordKey = '°'

class MouseInput:
    def __init__(self, typeOfInput, coordinateX, coordinateY):
        global count
        global recordTime
        self.order = count
        count += 1
        self.timing = time.time() - recordTime
        recordTime = time.time()
        self.typeOfInput = typeOfInput
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY

class KeyboardInput:
    def __init__(self, typeOfInput, key):
        global count
        global recordTime
        self.order = count
        count += 1
        self.timing = time.time() - recordTime
        recordTime = time.time()
        self.typeOfInput = typeOfInput
        self.key = key

# Create an array (list) and add the object
keyboard_array = []
mouse_array = []

def startRecording():
    global record
    global recordTime
    record = not record
    recordTime = time.time()
    print("Recording started")

def startPlayback():
    global endRecording
    global keyboard_array
    global mouse_array
    if pb.playbackState:
        pb.stopPlayback = True
        print("Playback stopped")
    else:
        playbackThread = threading.Thread(target=pb.playback, args=(keyboard_array, mouse_array), daemon=True)
        playbackThread.start()

def startReRecord():
    global count
    global recordTime
    global keyboard_array
    global mouse_array
    global record
    global stop
    global endRecording
    count = 0
    recordTime = time.time()
    keyboard_array = []
    mouse_array = []
    record = False
    stop = False
    endRecording = False
    print("Re-recording ready")

# KEYBOARD FUNCTIONS
def on_press(key):
    global keyboard_array
    if  hasattr(key, 'char') and key.char == recordKey:
        if not endRecording:
            startRecording()
        else:
            startPlayback()
    elif hasattr(key, 'char') and key.char == reRecordKey:
        startReRecord()

    if record:
        keyboard_array.append(KeyboardInput("Press", key))

def escapeActions():
    global endRecording
    global record
    endRecording = True
    record = False
    for element in keyboard_array:
        print(f"Order: {element.order},Timing: {element.timing} , Type: {element.typeOfInput}, Key: {element.key}")
    for element in mouse_array:
        print(f"Order: {element.order},Timing: {element.timing} , Type: {element.typeOfInput}, X: {element.coordinateX}, Y: {element.coordinateY}")


# This function is called every time a key is released
def on_release(key):
    # You can stop the listener by returning False
    if key == keyboard.Key.esc and not endRecording:
        escapeActions()
    elif key == keyboard.Key.esc and endRecording:
        print("test")
        global mouseEnd
        mouseEnd = True
        pyautogui.click()
        return False

def on_click(x, y, button, pressed):
    if mouseEnd:
        return False
    if pressed:
        if record:
            mouse_array.append(MouseInput("Click", x, y))