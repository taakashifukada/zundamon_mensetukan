import os
import pygame

class VoicePlayer:
    def __init__(self):
        pygame.mixer.init()

    def play(self, file_path):
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        else:
            print(f"File not found: {file_path}")
