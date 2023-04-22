import tkinter as tk
import random

class RandomTextDisplay:
    def __init__(self, master, list_of_strings):
        self.master = master
        self.remaining_strings = list_of_strings.copy()
        self.text_var = tk.StringVar()

        # Create and place label in the center of the white frame
        self.label = tk.Label(self.master, textvariable=self.text_var, font=("Helvetica", 24), bg="white")
        self.label.place(relx=0.5, rely=0.5, anchor="center")

        # Bind click event to the label
        self.label.bind("<Button-1>", self.display_random_text)

    def display_random_text(self, event):
        if self.remaining_strings:
            random_text = random.choice(self.remaining_strings)
            self.remaining_strings.remove(random_text)
            self.text_var.set(random_text)
        elif not self.text_var.get() == "END":
            self.text_var.set("END")
            self.master.unbind("<Button-1>")
            self.label.unbind("<Button-1>")


