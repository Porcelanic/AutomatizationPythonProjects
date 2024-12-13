import tkinter as tk


#To-do: The organization and readiblity of this file is AWFUL, everything needs to be organized and separated in modules

# Create the main window
root = tk.Tk()
root.title("Counter with Frame")
root.configure(bg="#E1AFD1")

x=1000 # Width of the window
y=800 # Height of the window

screen_width = root.winfo_screenwidth() # Get the screen width
screen_height = root.winfo_screenheight() # Get the screen height

# Calculate the x and y offsets to position the window at the center
w = (screen_width // 2) - (x // 2)
z = (screen_height // 2) - (y // 2)

root.geometry(f"+{w}+{z}")  # set the window offset from the top left corner of the screen

# Function to control fullscreen mode
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)
def enter_fullscreen(event=None):
    root.attributes("-fullscreen", True)

# Binding of the fullscreen functions to the 'Escape' and 'F' keys
root.bind("<Escape>", exit_fullscreen)
root.bind("<f>", enter_fullscreen)

# Create a canvas to act as a container
canvas = tk.Canvas(root, width=x, height=y, bg="#E1AFD1", highlightthickness=0)
canvas.pack_propagate(False)  # Prevent resizing to fit contents
canvas.pack() 

# Draw a vertical line through the middle
canvas.create_line(503, 0, 503, 800, fill="#000", width=6)

# Add a label inside the canvas
label = tk.Label(canvas, text="Off", font=("Arial", 24), bg="lightgray")
label.place(relx=0.25, rely=0.5, anchor="center")

# Function to increment the counter
def autoClikerFunction():
    label.config(text="On")


# Add a button inside the canvas 
button = tk.Button(canvas, text="Increment", command=increment, font=("Arial", 14), bg="#7469B6")
button.place(relx=0.25, rely=0.55, anchor="center")

# Run the GUI main loop
root.mainloop()
