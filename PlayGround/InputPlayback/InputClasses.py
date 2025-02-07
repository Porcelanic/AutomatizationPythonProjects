import time

class Input:
    def __init__(self, inType, state):
        self.inType = inType
        self.timing = time.time() - state.recordTime
        self.order = state.count
        state.count += 1
        state.recordTime = time.time()


class MouseInput:
    def __init__(self, typeOfInput, inputButton, coordinateX, coordinateY, state):
        self.input = Input("Mouse", state)
        self.typeOfInput = typeOfInput
        self.inputButton = inputButton
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY


class KeyboardInput:
    def __init__(self, typeOfInput, key, state):
        self.input = Input("Keyboard", state)
        self.typeOfInput = typeOfInput
        self.key = key