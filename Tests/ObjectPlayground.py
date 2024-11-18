# Define a class with 3 attributes
class MouseInput:
    def __init__(self, typeOfInput, coordinateX, coordinateY):
        self.typeOfInput = typeOfInput
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY

# Create an instance of the class
obj1 = MouseInput("Click", 100, 120)

# Create an array (list) and add the object
my_array = []
my_array.append(obj1)

# Add another object
obj2 = MouseInput("Click", 500, 220)
my_array.append(obj2)

# Access attributes
for obj in my_array:
    print(obj.typeOfInput, obj.coordinateX, obj.coordinateY)