import threading
from . import Recording as rc
from . import Playback as pb
from . import InputClasses as ic
from .Recording import state as Rstate
from .Playback import state as Pstate



# KEYBOARD FUNCTIONS
def KeyIsSpecial(key):
    if key == rc.RECORD_KEY:
        return True
    elif hasattr(key, "char") and (key.char == rc.RECORD_KEY or key.char == rc.RERECORD_KEY):
        return True
    return False

def handleKeyRecording(TypeOfInput, key):
    if not KeyIsSpecial(key):
        Pstate.array.append(ic.KeyboardInput(TypeOfInput, key, Rstate))


def handleOnPress(key):
    if Rstate.record:
        handleKeyRecording("Press", key)
    if hasattr(key, "char") and key.char == rc.RECORD_KEY:
        handleRecordKey()
    elif hasattr(key, "char") and key.char == rc.RERECORD_KEY:
        rc.startReRecord(Rstate)

def handleRecordKey():
    # checks if a recording is still possible and if it is, it changes the recording state
    if not rc.state.endRecording:
        rc.changeRecordingState(Rstate)
    else:
        # if a recording is not possible it instead starts handling the playback
        handlePlayback()    

def handlePlayback():
    if not Pstate.playbackState:
        Pstate.playbackState = True
        Pstate.stopPlayback = False
        playbackThread = threading.Thread(target=pb.playback, args=(Pstate,), daemon=True)
        playbackThread.start()
    else:
        Pstate.stopPlayback = True
        print("Playback stopped")

def handleOnRelease(key):
    if Rstate.record:
        handleKeyRecording("Release", key)
    return handleEscapeKey(key)

def handleEscapeKey(key):
    if key == rc.ESCAPE_KEY and not Rstate.endRecording:
        Rstate.endRecording = True
        printPlaybackArray()
    elif key == rc.ESCAPE_KEY and Rstate.endRecording:
        return False
    return True

def printPlaybackArray():
    for element in Pstate.array:
            if element.input.inType == "Keyboard":
                print(
                    f"Order: {element.input.order}, Type: {element.typeOfInput}, Key: {element.key}, timing: {element.input.timing}"
                )
            else:
                print(
                    f"Order: {element.input.order}, Type: {element.typeOfInput}, Button: {element.inputButton}, X: {element.coordinateX}, Y: {element.coordinateY}, timing: {element.input.timing}"
                )


# MOUSE FUNCTIONS
def handleMouseRecording(TypeOfInput, button, x, y):
    if Rstate.record:
        Pstate.array.append(ic.MouseInput(TypeOfInput, button, x, y, Rstate))


def handleOnClick(x, y, button, pressed):
    typeOfInput = "Click" if pressed else "Release"
    handleMouseRecording(typeOfInput, button, x, y)


def handleOnMove(x, y):
    handleMouseRecording("Move", "None", x, y)