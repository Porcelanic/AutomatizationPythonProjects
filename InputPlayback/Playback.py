import pyautogui  # Perform actions like clicks
import time


class playbackState:
    def __init__(self):
        self.playbackState = False
        self.stopPlayback = False
        self.array = []


state = playbackState()


def waitAndDoKeyboard(action, timing, inputType):
    time.sleep(timing * 0.4)
    if inputType == "Press":
        pyautogui.keyDown(action)
    else:
        pyautogui.keyUp(action)

def keyboardPlayback(order):
    keyAction = state.array[order]
    if hasattr(keyAction.key, "char") and keyAction.key.char != "|":
        waitAndDoKeyboard(keyAction.key.char, keyAction.input.timing, keyAction.typeOfInput)
    elif not hasattr(keyAction.key, "char") and keyAction.key.name != "esc":
        key = keyAction.key.name.replace("_", "")
        waitAndDoKeyboard(key, keyAction.input.timing, keyAction.typeOfInput)


def mousePlayback(order):
    mouseAction = state.array[order]
    pyautogui.moveTo(mouseAction.coordinateX, mouseAction.coordinateY)
    if mouseAction.typeOfInput == "Click":
        pyautogui.mouseDown()
    elif mouseAction.typeOfInput == "Release":
        pyautogui.mouseUp()

def playback():
    global state
    state.playbackState = True
    print("Playback will start in 2 seconds")
    time.sleep(2)
    print("Playback started")
    end = state.array[-1].input.order
    order = 0
    while order <= end and not state.stopPlayback:
        action = state.array[order]
        if action.input.inType == "Keyboard":
            keyboardPlayback(order)
        else:
            mousePlayback(order)
        order += 1
    state.stopPlayback = False
    state.playbackState = False
    print("Playback ended")
