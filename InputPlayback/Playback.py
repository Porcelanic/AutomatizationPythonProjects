import pyautogui  # Perform actions like clicks
import time

playbackState = False
stopPlayback = False

def waitAndDoKeyboard(action, timing):
    time.sleep(timing)
    pyautogui.press(action)

def keyboardPlayback(keyboard_array, currentKeyboardIndex):
    keyAction = keyboard_array[currentKeyboardIndex]
    if keyAction.typeOfInput == "Press":
        if hasattr(keyAction.key, "char") and keyAction.key.char != "|":
            waitAndDoKeyboard(keyAction.key.char, keyAction.timing)
        elif not hasattr(keyAction.key, "char") and keyAction.key.name != "esc":
            key = keyAction.key.name.replace("_", "")
            waitAndDoKeyboard(key, keyAction.timing)
    currentKeyboardIndex += 1
    return currentKeyboardIndex

def mousePlayback(mouse_array, currentMouseIndex):
    mouseAction = mouse_array[currentMouseIndex]
    time.sleep(mouseAction.timing*0.4)
    pyautogui.moveTo(mouseAction.coordinateX, mouseAction.coordinateY)
    if mouseAction.typeOfInput == "Click":
        pyautogui.click()
    currentMouseIndex += 1
    return currentMouseIndex


def playback(keyboard_array, mouse_array):
    global playbackState
    global stopPlayback
    playbackState = True
    print("Playback will start in 2 seconds")
    time.sleep(2)
    print("Playback started")
    end = 0
    if len(keyboard_array) == 0 and len(mouse_array) == 0:
        print("No inputs to playback")
        return
    elif len(keyboard_array) == 0:
        end = mouse_array[-1].order
    elif len(mouse_array) == 0:
        end = keyboard_array[-1].order
    else:
        if keyboard_array[-1].order > mouse_array[-1].order:
            end = keyboard_array[-1].order
        else:
            end = mouse_array[-1].order
    order = 0
    currentKeyboardIndex = 0
    currentMouseIndex = 0
    while order <= end and not stopPlayback:
        if currentKeyboardIndex < len(keyboard_array) and keyboard_array[currentKeyboardIndex].order == order:
            currentKeyboardIndex = keyboardPlayback(keyboard_array, currentKeyboardIndex)
        else:
            if currentMouseIndex < len(mouse_array) and mouse_array[currentMouseIndex].order == order:
                currentMouseIndex = mousePlayback(mouse_array, currentMouseIndex)
        order += 1
    stopPlayback = False
    playbackState = False
    print("Playback ended")
