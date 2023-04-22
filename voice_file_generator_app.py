import tkinter as tk
from voice_file_generator import VoiceFileGenerator
from text_file_reader import TextFileReader

class VoiceFileGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.generate_button = tk.Button(self.frame, text="Generate Voice Files", command=self.generate_voice_files)
        self.generate_button.pack(pady=10)

    def generate_voice_files(self):
        text_file_reader = TextFileReader("plot.txt")
        list_of_strings = text_file_reader.read_strings()
        voice_file_generator = VoiceFileGenerator(list_of_strings)
        voice_file_generator.generate_voice_files()

