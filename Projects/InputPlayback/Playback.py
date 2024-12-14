import pyautogui  # Perform actions like clicks
import time

useTiming = True


class playbackState:
    def __init__(self):
        self.playbackState = False
        self.stopPlayback = False
        self.array = []


state = playbackState()


# this functions applies the DRY principle
def waitAndDoKeyboard(action, inputType):
    if inputType == "Press":
        pyautogui.keyDown(action)
    else:
        pyautogui.keyUp(action)

# handles the playback of the keyboard actions
def keyboardPlayback(keyAction):
    if keyAction.hasChar:
        waitAndDoKeyboard(keyAction.key.char, keyAction.typeOfInput)
    else:
        waitAndDoKeyboard(keyAction.key.name.replace("_", ""), keyAction.typeOfInput)

# handles the playback of the mouse actions
def mousePlayback(mouseAction):
    pyautogui.moveTo(mouseAction.coordinateX, mouseAction.coordinateY)
    if mouseAction.typeOfInput == "Click":
        pyautogui.mouseDown()
    elif mouseAction.typeOfInput == "Release":
        pyautogui.mouseUp()

# starts the playback of the actions
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

# this is the function that is used to create a thread for the playback
def playback():
    global state
    state.stopPlayback = False
    # if useTiming is true, the default pause from pyautogui is set to 0, 
    # if not, it is set to 0.01 (since saying to pyautogui to not pause at all can cause some problems)
    if useTiming:
        pyautogui.PAUSE = 0
    else:
        pyautogui.PAUSE = 0.01
    print("Playback will start in 0.5 seconds")
    state.playbackState = True
    time.sleep(0.5)
    startPlayback(state)
    state.stopPlayback = False
    state.playbackState = False
    print("Playback ended")
