import time
from Playback import state as Pstate
from pynput import keyboard

RECORD_KEY = "-"
RERECORD_KEY = "_"
ESCAPE_KEY = keyboard.Key.esc

class RecordingState:
    def __init__(self):
        self.count = 0
        self.endRecording = False
        self.record = False
        self.recordTime = time.time()

state = RecordingState()

def changeRecordingState(state):
    state.record = not state.record
    if state.record:
        state.recordTime = time.time()
        print("Recording started")
    else:
        print("Recording stopped")

def startReRecord(state):
    state.count = 0
    Pstate.array = []
    state.record = False
    state.endRecording = False
    Pstate.stopPlayback =  True
    print("Re-recording ready")