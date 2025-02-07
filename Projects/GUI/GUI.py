import tkinter as tk
from .AutoClickerFrame import AutoClickerFrame
from .PlaybackFrame import PlaybackFrame
from .WindowManager import WindowManager

class MainApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Input Automation Tool")
        self.root.configure(bg="#E1AFD1")
        
        # Initialize window manager
        self.window_manager = WindowManager(self.root)
        self.setup_window()
        
        # Create main canvas
        self.canvas = self.create_main_canvas()
        self.draw_divider()
        
        # Initialize frames
        self.autoclicker_frame = AutoClickerFrame(self.canvas)
        self.playback_frame = PlaybackFrame(self.canvas)
        
    def setup_window(self):
        self.window_manager.center_window(1000, 800)
        self.window_manager.setup_fullscreen_bindings()
    
    def create_main_canvas(self):
        canvas = tk.Canvas(
            self.root,
            width=1000,
            height=800,
            bg="#E1AFD1",
            highlightthickness=0
        )
        canvas.pack_propagate(False)
        canvas.pack()
        return canvas
    
    def draw_divider(self):
        self.canvas.create_line(503, 0, 503, 800, fill="#000", width=6)
    
    def run(self):
        self.root.mainloop()

def main():
    app = MainApplication()
    app.run()

if __name__ == "__main__":
    main()