import pyautogui  # Perform actions like clicks
import time


class playbackState:
    def __init__(self):
        self.playbackState = False
        self.stopPlayback = False
        self.keyboard_array = []
        self.mouse_array = []


state = playbackState()


def waitAndDoKeyboard(action, timing):
    time.sleep(timing * 0.4)
    pyautogui.press(action)


def keyboardPlayback(currentKeyboardIndex):
    keyAction = state.keyboard_array[currentKeyboardIndex]
    if keyAction.typeOfInput == "Press":
        if hasattr(keyAction.key, "char") and keyAction.key.char != "|":
            waitAndDoKeyboard(keyAction.key.char, keyAction.timing)
        elif not hasattr(keyAction.key, "char") and keyAction.key.name != "esc":
            key = keyAction.key.name.replace("_", "")
            waitAndDoKeyboard(key, keyAction.timing)
    currentKeyboardIndex += 1
    return currentKeyboardIndex


def mousePlayback(currentMouseIndex):
    mouseAction = state.mouse_array[currentMouseIndex]
    time.sleep(mouseAction.timing * 0.4)
    pyautogui.moveTo(mouseAction.coordinateX, mouseAction.coordinateY)
    if mouseAction.typeOfInput == "Click":
        pyautogui.click()
    currentMouseIndex += 1
    return currentMouseIndex


def playback():
    global state
    state.playbackState = True
    print("Playback will start in 2 seconds")
    time.sleep(2)
    print("Playback started")
    end = 0
    if len(state.keyboard_array) == 0 and len(state.mouse_array) == 0:
        print("No inputs to playback")
        return
    elif len(state.keyboard_array) == 0:
        end = state.mouse_array[-1].order
    elif len(state.mouse_array) == 0:
        end = state.keyboard_array[-1].order
    else:
        if state.keyboard_array[-1].order > state.mouse_array[-1].order:
            end = state.keyboard_array[-1].order
        else:
            end = state.mouse_array[-1].order
    order = 0
    currentKeyboardIndex = 0
    currentMouseIndex = 0
    while order <= end and not state.stopPlayback:
        if (
            currentKeyboardIndex < len(state.keyboard_array)
            and state.keyboard_array[currentKeyboardIndex].order == order
        ):
            currentKeyboardIndex = keyboardPlayback(currentKeyboardIndex)
        else:
            if (
                currentMouseIndex < len(state.mouse_array)
                and state.mouse_array[currentMouseIndex].order == order
            ):
                currentMouseIndex = mousePlayback(currentMouseIndex)
        order += 1
    state.stopPlayback = False
    state.playbackState = False
    print("Playback ended")
