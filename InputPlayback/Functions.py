from pynput import keyboard
import threading
import pyautogui
import time
import Playback as pb

RECORD_KEY = "|"
RERECORD_KEY = "°"
ESCAPE_KEY = keyboard.Key.esc


class RecordingState:
    def __init__(self):
        self.count = 0
        self.endRecording = False
        self.record = False
        self.mouseEnd = False
        self.recordTime = time.time()
        self.keyboard_array = []
        self.mouse_array = []


class MouseInput:
    def __init__(self, typeOfInput, coordinateX, coordinateY):
        global state
        self.order = state.count
        state.count += 1
        self.timing = time.time() - state.recordTime
        state.recordTime = time.time()
        self.typeOfInput = typeOfInput
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY


class KeyboardInput:
    def __init__(self, typeOfInput, key):
        global state
        self.order = state.count
        state.count += 1
        self.timing = time.time() - state.recordTime
        state.recordTime = time.time()
        self.typeOfInput = typeOfInput
        self.key = key


state = RecordingState()


def changeRecordingState():
    global state
    state.record = not state.record
    state.recordTime = time.time()
    if state.record:
        print("Recording started")
    else:
        print("Recording stopped")


def startPlayback():
    global state
    if pb.state.playbackState:
        pb.state.stopPlayback = True
        print("Playback stopped")
    else:
        playbackThread = threading.Thread(target=pb.playback, daemon=True)
        playbackThread.start()


def startReRecord():
    global state
    state.count = 0
    state.recordTime = time.time()
    pb.state.keyboard_array = []
    pb.state.mouse_array = []
    state.record = False
    state.stop = False
    state.endRecording = False
    print("Re-recording ready")


# KEYBOARD FUNCTIONS
def on_press(key):
    print(f"{key} pressed")
    if hasattr(key, "char") and key.char == RECORD_KEY:
        if not state.endRecording:
            changeRecordingState()
        else:
            startPlayback()
    elif hasattr(key, "char") and key.char == RERECORD_KEY:
        startReRecord()

    if state.record:
        pb.state.keyboard_array.append(KeyboardInput("Press", key))


def escapeActions():
    global state
    state.endRecording = True
    state.record = False
    for element in pb.state.keyboard_array:
        print(
            f"Order: {element.order},Timing: {element.timing} , Type: {element.typeOfInput}, Key: {element.key}"
        )
    for element in pb.state.mouse_array:
        print(
            f"Order: {element.order},Timing: {element.timing} , Type: {element.typeOfInput}, X: {element.coordinateX}, Y: {element.coordinateY}"
        )


# This function is called every time a key is released
def on_release(key):
    global state
    # You can stop the listener by returning False
    if key == ESCAPE_KEY and not state.endRecording:
        escapeActions()
    elif key == ESCAPE_KEY and state.endRecording:
        state.mouseEnd = True
        pyautogui.click()
        return False


def on_click(x, y, button, pressed):
    if state.mouseEnd:
        return False
    if pressed:
        if state.record:
            pb.state.mouse_array.append(MouseInput("Click", x, y))
