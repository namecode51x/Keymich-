import pygame
import random
import os

class SoundManager:
    def __init__(self, route):
        self.route = route
        pygame.mixer.init()
        self.list = []
        self.list_exluide = ["space.wav", "backspace.wav", "esc.wav", "right shift.wav"]
        self.list_especial = ["space", "backspace", "esc", "right shift"]
        self.key_especial = {}

    def search_sounds(self):
        for i in os.listdir(self.route):
            if i.endswith(".wav") and not i in self.list_exluide:
                self.keyboard = i.replace(".wav", "")
                sound_change = pygame.mixer.Sound(self.route + '/' + i)
                self.list.append(sound_change)

    def load_sound_special(self):
        for i in self.list_especial:
            self.key_especial[i] = pygame.mixer.Sound(self.route + "/" + i + ".wav")


    def play_sound(self, key):
         if key in self.key_especial:
           self.sound = self.key_especial.get(key)
           self.sound.play()
         else:
            self.sound_ = random.choice(self.list)
            self.sound_.play()