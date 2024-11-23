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
        self.array = []
        self.currentMouseXPossition = 0
        self.currentMouseYPossition = 0


class Input:
    def __init__(self, inType, order, timing):
        self.inType = inType
        self.order = order
        self.timing = timing
        state.count += 1
        state.recordTime = time.time()


class MouseInput:
    def __init__(self, typeOfInput, inputButton, coordinateX, coordinateY):
        global state
        self.input = Input("Mouse", state.count, time.time() - state.recordTime)
        self.typeOfInput = typeOfInput
        self.inputButton = inputButton
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY


class KeyboardInput:
    def __init__(self, typeOfInput, key):
        global state
        self.input = Input("Keyboard", state.count, time.time() - state.recordTime)
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
    pb.state.array = []
    pb.state.array = []
    state.record = False
    state.stop = False
    state.endRecording = False
    print("Re-recording ready")


# KEYBOARD FUNCTIONS
def on_press(key):
    if hasattr(key, "char") and key.char == RECORD_KEY:
        if not state.endRecording:
            changeRecordingState()
        else:
            startPlayback()
    elif hasattr(key, "char") and key.char == RERECORD_KEY:
        startReRecord()

    if state.record:
        pb.state.array.append(KeyboardInput("Press", key))


def escapeActions():
    global state
    state.endRecording = True
    state.record = False
    for element in pb.state.array:
        if element.input.inType == "Keyboard":
            print(
                f"Order: {element.input.order},Timing: {element.input.timing} , Type: {element.typeOfInput}, Key: {element.key}"
            )
        else:
            print(
                f"Order: {element.input.order},Timing: {element.input.timing} , Type: {element.typeOfInput}, X: {element.coordinateX}, Y: {element.coordinateY}"
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
    if state.record:
        pb.state.array.append(KeyboardInput("Release", key))


def on_click(x, y, button, pressed):
    if state.mouseEnd:
        return False
    if state.record:
        if pressed:
            pb.state.array.append(MouseInput("Click", button, x, y))
        else:
            pb.state.array.append(MouseInput("Release", button, x, y))


def inRange(X, Y):
    rangeConstant = 75
    if (
        state.currentMouseXPossition - rangeConstant
        <= X
        <= state.currentMouseXPossition + rangeConstant
        and state.currentMouseYPossition - rangeConstant
        <= Y
        <= state.currentMouseYPossition + rangeConstant
    ):
        return True
    return False


def on_move(x, y):
    if state.record and not inRange(x, y):
        state.currentMouseXPossition = x
        state.currentMouseYPossition = y
        pb.state.array.append(MouseInput("Move", "None", x, y))
