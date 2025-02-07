import pyautogui  # Perform actions like clicks
import time
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

useTiming = True
pyautogui.PAUSE = 0

Keyboard = KeyboardController()
Mouse = MouseController()


class playbackState:
    def __init__(self):
        self.playbackState = False
        self.stopPlayback = False
        self.array = []

state = playbackState()


# handles the playback of the keyboard actions
def keyboardPlayback(keyAction):
    if keyAction.typeOfInput == "Press":
        Keyboard.press(keyAction.key)
    else:
        Keyboard.release(keyAction.key)


pressing = False

# handles the playback of the mouse actions
def mousePlayback(mouseAction):
    global pressing
    if not pressing:
        Mouse.position = (mouseAction.coordinateX, mouseAction.coordinateY)
    else:
        pyautogui.dragTo(mouseAction.coordinateX, mouseAction.coordinateY)
    if mouseAction.typeOfInput == "Click":
        Mouse.press(Button.left)
        pressing = True
    elif mouseAction.typeOfInput == "Release":
        Mouse.release(Button.left)
        pressing = False


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
def playback(state):
    print("Playback will start in 0.5 seconds")
    time.sleep(0.5)
    startPlayback(state)
    state.stopPlayback = False
    state.playbackState = False
    print("Playback ended")