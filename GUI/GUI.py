import tkinter as tk
from AutoClickerProyect import AutoClicker as ac
import threading

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

#Left half corresponding to the AutoClicker Script

# Add a label inside the canvas
label = tk.Label(canvas, text="OFF", font=("Arial", 24), bg="lightgray")
label.place(relx=0.25, rely=0.25, anchor="center")

clicker = threading.Thread(target=ac.main, daemon=True)
clicker.start()

# Function to enable the auto clicker
def autoClikerFunction():
    if label.cget("text") == "OFF":
        label.config(text="ON")
        button.config(text="Deactivate")
        ac.enableAutoClicker(True)
    else:
        label.config(text="OFF")
        button.config(text="Activate")
        ac.enableAutoClicker(False)

# Add a button inside the canvas 
button = tk.Button(canvas, text="Activate", command=autoClikerFunction, font=("Arial", 14), bg="#7469B6")
button.place(relx=0.25, rely=0.3, anchor="center")

# Add labels with information about the auto clicker
labelClickerHeader = tk.Label(canvas, text="When the autoclicker is 'ON'", font=("Arial", 14), bg="#E1AFD1")
labelClickerHeader.place(relx=0.25, rely=0.45, anchor="center")
labelClickerInfo1 = tk.Label(canvas, text="Press 'c' to start clicking", font=("Arial", 14), bg="#E1AFD1")
labelClickerInfo1.place(relx=0.25, rely=0.5, anchor="center")
labelClickerInfo2 = tk.Label(canvas, text="Press 'v' to stop clicking", font=("Arial", 14), bg="#E1AFD1")
labelClickerInfo2.place(relx=0.25, rely=0.55, anchor="center")
labelClickerInfo3 = tk.Label(canvas, text="Keep in mind 'c' and 'C' ARE different", font=("Arial", 14), bg="#E1AFD1")
labelClickerInfo3.place(relx=0.25, rely=0.6, anchor="center")

# Right half corresponding to a work in progress
# Add a label inside the canvas
playbackLabel = tk.Label(canvas, text="Work in progress", font=("Arial", 24), bg="lightgray")
playbackLabel.place(relx=0.75, rely=0.25, anchor="center")

# Add a button inside the canvas 
playbackButton = tk.Button(canvas, text="Work in progress", font=("Arial", 14), bg="#7469B6")
playbackButton.place(relx=0.75, rely=0.3, anchor="center")

# Add labels with information about the auto playback
labelPlaybackHeader = tk.Label(canvas, text="Work in progress", font=("Arial", 14), bg="#E1AFD1")
labelPlaybackHeader.place(relx=0.75, rely=0.45, anchor="center")
labelPlaybackInfo1 = tk.Label(canvas, text="Work in progress", font=("Arial", 14), bg="#E1AFD1")
labelPlaybackInfo1.place(relx=0.75, rely=0.5, anchor="center")
labelPlaybackInfo2 = tk.Label(canvas, text="Work in progress", font=("Arial", 14), bg="#E1AFD1")
labelPlaybackInfo2.place(relx=0.75, rely=0.55, anchor="center")
labelPlaybackInfo3 = tk.Label(canvas, text="Work in progress", font=("Arial", 14), bg="#E1AFD1")
labelPlaybackInfo3.place(relx=0.75, rely=0.6, anchor="center")

# Run the GUI main loop
root.mainloop()
