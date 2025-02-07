import ListenersControllers as c

killSwitch = False
main = False

def setKillSwitch(state):
    global killSwitch
    killSwitch = state

# KEYBOARD FUNCTIONS
def on_press(key):
    if killSwitch:
        return False
    #print(f"{key} pressed")
    c.handleOnPress(key)
    

# This function is called every time a key is released
def on_release(key):
    #print(f"{key} released")
    if not c.handleOnRelease(key) and main:
        return False
 
def on_click(x, y, button, pressed):
    #if pressed:
        #print(f"{button} pressed at {x}, {y}")
    #else:
        #print(f"{button} released at {x}, {y}")
    c.handleOnClick(x, y, button, pressed)

def on_move(x, y):
    if killSwitch:
        return False
    #print(f"Mouse moved to {x}, {y}")
    c.handleOnMove(x, y)

