import Playback as pb
import Recording as rc
import InputClasses as ic


# KEYBOARD FUNCTIONS
def on_press(key):
    # checks if the key is either the record (or re-record) key or escape key and if it is it doesn't record it
    if rc.state.record and not rc.KeyIsSpecial(key):
        # adds the key press to the array
        pb.state.array.append(ic.KeyboardInput("Press", key, rc.state))

    # checks if the key is the record key
    if hasattr(key, "char") and key.char == rc.RECORD_KEY:
        # checks if a recording is still possible and if it is it changes the recording state
        if not rc.state.endRecording:
            rc.changeRecordingState()
        else:
            # if a recording is not possible it starts the playback
            rc.startPlayback()

    # checks if the key is the re-record key and if it is it starts the re-recording
    elif hasattr(key, "char") and key.char == rc.RERECORD_KEY:
        rc.startReRecord()


def on_release(key):
    # checks if the key is the escape key and if it is it calls the escape actions
    if key == rc.ESCAPE_KEY:
        # checks if the recording has ended and if it has it returns False
        if rc.state.endRecording:
            return False  # this return statement is the way the program exits
        else:
            rc.escapeActions()

    # checks if the key is a special key and if it is it doesn't record it
    if rc.state.record and not rc.KeyIsSpecial(key):
        # adds the key release to the array
        pb.state.array.append(ic.KeyboardInput("Release", key, rc.state))


# MOUSE FUNCTIONS
def on_click(x, y, button, pressed):
    # checks if the recording is active and if it is it adds the mouse input to the array
    if rc.state.record:
        if pressed:
            pb.state.array.append(ic.mouseInput("Click", button, x, y, rc.state))
        else:
            pb.state.array.append(ic.mouseInput("Release", button, x, y, rc.state))


def on_move(x, y):
    # checks if the recording is active and  the mouse is outside a cetain range and if it is, it adds the mouse movement to the array
    # the range restriction was added so that the mouse movement wouldn't monopolize the input array
    # since one normal motion of the mouse would create a crazy amount of inputs
    if rc.state.record and not rc.inRange(x, y):
        rc.state.currentMouseXPossition = x
        rc.state.currentMouseYPossition = y
        pb.state.array.append(ic.mouseInput("Move", "None", x, y, rc.state))
