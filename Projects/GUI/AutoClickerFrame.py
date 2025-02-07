import tkinter as tk
import threading
from AutoClickerProject import AutoClicker as ac

class AutoClickerFrame:
    def __init__(self, canvas):
        self.canvas = canvas
        self.setup_ui()
        self.start_autoclicker_thread()
    
    def setup_ui(self):
        # Header
        self.create_label("AUTOCLICKER", 0.25, 0.15, 24)
        self.status_label = self.create_label("OFF", 0.25, 0.25, 24)
        
        # Activation button
        self.button = tk.Button(
            self.canvas,
            text="Activate",
            command=self.toggle_autoclicker,
            font=("Arial", 12),
            bg="#7469B6"
        )
        self.button.place(relx=0.25, rely=0.3, anchor="center")
        
        # Info labels
        self.create_info_labels()
    
    def create_label(self, text, relx, rely, size):
        label = tk.Label(
            self.canvas,
            text=text,
            font=("Arial", size),
            bg="lightgray"
        )
        label.place(relx=relx, rely=rely, anchor="center")
        return label
    
    def create_info_labels(self):
        info_texts = [
            ("When the autoclicker is 'ON'", 0.45),
            ("Press 'c' to start clicking", 0.5),
            ("Press 'v' to stop clicking", 0.55),
            ("Keep in mind 'c' and 'C' ARE different", 0.6)
        ]
        
        for text, rely in info_texts:
            tk.Label(
                self.canvas,
                text=text,
                font=("Arial", 12),
                bg="#E1AFD1"
            ).place(relx=0.25, rely=rely, anchor="center")
    
    def start_autoclicker_thread(self):
        self.clicker_thread = threading.Thread(
            target=ac.main,
            daemon=True
        )
        self.clicker_thread.start()
    
    def toggle_autoclicker(self):
        if self.status_label.cget("text") == "OFF":
            self.status_label.config(text="ON")
            self.button.config(text="Deactivate")
            ac.enableAutoClicker(True)
        else:
            self.status_label.config(text="OFF")
            self.button.config(text="Activate")
            ac.enableAutoClicker(False)