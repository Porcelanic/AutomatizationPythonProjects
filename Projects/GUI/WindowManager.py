class WindowManager:
    def __init__(self, root):
        self.root = root
    
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        self.root.geometry(f"+{x}+{y}")
    
    def setup_fullscreen_bindings(self):
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))
        self.root.bind("<f>", lambda e: self.root.attributes("-fullscreen", True))