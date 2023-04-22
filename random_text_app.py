import tkinter as tk
import random
from tkinter import ttk
from text_file_reader import TextFileReader
from audio_recorder import AudioRecorder
from voice_player import VoicePlayer

class RandomTextApp:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)

        text_file_reader = TextFileReader("plot.txt")
        self.list_of_strings = text_file_reader.read_strings()
        self.remaining_strings = self.list_of_strings.copy()

        self.text_var = tk.StringVar()
        self.text_var.set("START")

        self.label = tk.Label(self.frame, textvariable=self.text_var, bg="white", font=("Arial", 30))
        self.label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.frame.bind("<Button-1>", self.on_click)

        self.audio_recorder = AudioRecorder()

        self.record_button_style = ttk.Style()
        self.record_button_style.configure("Record.TButton", background="green", relief=tk.RAISED)
        self.record_button = ttk.Button(self.frame, text="▶", style="Record.TButton", command=self.toggle_recording)
        self.record_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.voice_player = VoicePlayer()

        self.play_audio_var = tk.BooleanVar()
        self.play_audio_var.set(False)

        self.play_audio_checkbox = tk.Checkbutton(self.frame, text="Play audio", variable=self.play_audio_var, bg="white")
        self.play_audio_checkbox.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def on_click(self, event):
        if not self.remaining_strings:
            return
        if self.text_var.get() == "START":
            new_text = random.choice(self.remaining_strings)
            self.text_var.set(new_text)
            self.remaining_strings.remove(new_text)
        else:
            new_text = random.choice(self.remaining_strings)
            self.text_var.set(new_text)
            self.remaining_strings.remove(new_text)
            if not self.remaining_strings:
                self.text_var.set("END")
        if self.play_audio_var.get():
            audio_file = f"voice_files/{self.text_var.get()}.wav"
            self.voice_player.play(audio_file)


    def toggle_recording(self):
        if not self.audio_recorder.is_recording:
            self.audio_recorder.start_recording()
            self.record_button_style.configure("Record.TButton", background="red")
            self.record_button.config(text="■")
        else:
            self.audio_recorder.stop_recording()
            self.record_button_style.configure("Record.TButton", background="green")
            self.record_button.config(text="▶")
