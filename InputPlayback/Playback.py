import pyautogui  # Perform actions like clicks
import time

useTiming = True


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


def startPlayback(state):
    state.playbackState = True
    print("Playback started")
    for i in range(len(state.array)):
        if state.stopPlayback:
            break
        element = state.array[i]
        if useTiming:
            time.sleep(element.input.timing)
        if element.input.inType == "Keyboard":
            keyboardPlayback(element)
        else:
            mousePlayback(element)


def playback():
    global state
    if useTiming:
        pyautogui.PAUSE = 0
    else:
        pyautogui.PAUSE = 0.01
    print("Playback will start in 2 seconds")
    time.sleep(2)
    startPlayback(state)
    state.stopPlayback = False
    state.playbackState = False
    print("Playback ended")
