from keyboard import play
import pygame
import random
import os

class SoundManager:
    def __init__(self, route, route_keyboards):
        self.route_keyboards = route_keyboards
        self.route = route
        self.sound_start = "assets/sound_start/Start_app.wav"
        pygame.mixer.init()
        self.sound_fire = pygame.mixer.Sound(self.sound_start)

        # Listas
        self.list = []
        self.list_exluide = ["space.wav", "backspace.wav", "esc.wav", "right shift.wav"]
        self.list_especial = ["space", "backspace", "esc", "right shift"]
        self.key_especial = {}
        self.list_keybords = []

    def search_sounds(self):
        for i in os.listdir(self.route):
            if i.endswith(".wav") and not i in self.list_exluide:
                self.keyboard = i.replace(".wav", "")
                sound_change = pygame.mixer.Sound(self.route + '/' + i)
                self.list.append(sound_change)
    
    def search_keybords(self):
        for i in os.listdir(self.route_keyboards):
            if os.path.isdir(self.route_keyboards + "/" + i):
              self.list_keybords.append(i)

        #* Change the Keybord Sound
    def change_keyboard(self, new_pack_name):
        self.route = self.route_keyboards + "/" + new_pack_name
        self.list = []
        self.search_sounds()
        self.key_especial = {}
        self.load_sound_special()

    def start_app(self):
        self.sound_fire.play()

    def load_sound_special(self):
        for i in self.list_especial:
            self.key_especial[i] = pygame.mixer.Sound(self.route + "/" + i + ".wav")

        # Play the Keybord Sound    
    def play_sound(self, key):
         if key in self.key_especial:
           self.sound = self.key_especial.get(key)
           self.sound.play()
         else:
            self.sound_ = random.choice(self.list)
            self.sound_.play()