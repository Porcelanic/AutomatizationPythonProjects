from pynput import keyboard
import threading
from . import Playback as pb
import time

RECORD_KEY = "|"
RERECORD_KEY = "°"
ESCAPE_KEY = keyboard.Key.esc


class RecordingState:
    def __init__(self):
        self.count = 0
        self.endRecording = False
        self.record = False
        self.array = []
        self.recordTime = time.time()
        self.currentMouseXPossition = 0
        self.currentMouseYPossition = 0


state = RecordingState()


def changeRecordingState():
    global state
    state.record = not state.record
    if state.record:
        state.recordTime = time.time()
        print("Recording started")
    else:
        print("Recording stopped")


def stopPlayback():
    pb.state.stopPlayback = True

def startPlayback():
    global state
    if pb.state.playbackState:
        stopPlayback()
    else:
        playbackThread = threading.Thread(target=pb.playback, daemon=True)
        playbackThread.start()


def startReRecord():
    global state
    state.count = 0
    pb.state.array = []
    pb.state.array = []
    state.record = False
    state.stop = False
    state.endRecording = False
    stopPlayback()
    print("Re-recording ready")


def KeyIsSpecial(key):
    if hasattr(key, "char") and key.char == RECORD_KEY:
        return True
    elif not hasattr(key, "char") and key.name == "esc":
        return True
    return False


def escapeActions():
    global state
    state.endRecording = True
    state.record = False
    for element in pb.state.array:
        if element.input.inType == "Keyboard":
            print(
                f"Order: {element.input.order}, Type: {element.typeOfInput}, Key: {element.key}, timing: {element.input.timing}"
            )
        else:
            print(
                f"Order: {element.input.order}, Type: {element.typeOfInput}, X: {element.coordinateX}, Y: {element.coordinateY}, timing: {element.input.timing}"
            )


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
