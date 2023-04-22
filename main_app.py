import tkinter as tk
from random_text_app import RandomTextApp
from voice_file_generator_app import VoiceFileGeneratorApp
from navigation import Navigation

class MainApp:
    def __init__(self, master):
        self.master = master
        self.navigation = Navigation(self.master, RandomTextApp, VoiceFileGeneratorApp)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = MainApp(root)
    root.mainloop()



