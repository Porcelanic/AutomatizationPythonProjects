import pyautogui  # Perform actions like clicks
import time

pyautogui.PAUSE = 0.01

class playbackState:
    def __init__(self):
        self.playbackState = False
        self.stopPlayback = False
        self.array = []


state = playbackState()


def waitAndDoKeyboard(action, inputType):
    if inputType == "Press":
        pyautogui.keyDown(action)
    else:
        pyautogui.keyUp(action)

def keyboardPlayback(keyAction):
    if keyAction.hasChar:
        waitAndDoKeyboard(keyAction.key.char, keyAction.typeOfInput)
    else:
        waitAndDoKeyboard(keyAction.key.name.replace("_", ""), keyAction.typeOfInput)


def mousePlayback(mouseAction):
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
    for i in range(len(state.array)):
        if state.stopPlayback:
            break
        element = state.array[i]
        if element.input.inType == "Keyboard":
            keyboardPlayback(element)
        else:
            mousePlayback(element)
    state.stopPlayback = False
    state.playbackState = False
    print("Playback ended")
