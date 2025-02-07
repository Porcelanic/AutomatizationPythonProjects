import tkinter as tk
import threading
from InputPlayback import Launcher as ip

class PlaybackFrame:
    def __init__(self, canvas):
        self.canvas = canvas
        self.setup_ui()
        self.start_playback_thread()
    
    def setup_ui(self):
        # Header
        self.create_label("INPUT RECORDER-PLAYBACK", 0.75, 0.15, 24)
        self.status_label = self.create_label("OFF", 0.75, 0.25, 24)
        
        # Activation button
        self.button = tk.Button(
            self.canvas,
            text="Activate",
            command=self.toggle_playback,
            font=("Arial", 12),
            bg="#7469B6"
        )
        self.button.place(relx=0.75, rely=0.3, anchor="center")
        
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
            ("When the Input Playbacker is 'ON' it starts in 'Recording Mode'", 0.45),
            ("Press '|' to start recording your inputs", 0.5),
            ("Press '|' again to stop the recording", 0.55),
            ("Press 'esc' to enable the 'Playback Mode'", 0.6),
            ("When the 'playback' has been enabled", 0.65),
            ("Press '|' to start playing back the inputs you recorded before", 0.7),
            ("Press '|' again to stop the playback", 0.75),
            ("Press '°' to go back to Recording Mode", 0.8)
        ]
        
        for text, rely in info_texts:
            tk.Label(
                self.canvas,
                text=text,
                font=("Arial", 12),
                bg="#E1AFD1"
            ).place(relx=0.75, rely=rely, anchor="center")
    
    def start_playback_thread(self):
        self.playback_thread = threading.Thread(
            target=ip.guiThread,
            daemon=True
        )
        self.playback_thread.start()
    
    def toggle_playback(self):
        if self.status_label.cget("text") == "OFF":
            self.status_label.config(text="ON")
            self.button.config(text="Deactivate")
            ip.gui_wait_event.set()
        else:
            self.status_label.config(text="OFF")
            self.button.config(text="Activate")
            ip.killThreads()