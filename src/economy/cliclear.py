import keyboard
import threading as thr
class Clickear:
    def __init__(self, wallet, sound):
        self.sound = sound
        self.keychaps = wallet
        self.helper = None
        self.active = False
        self.list = []

    #! Enciende al Ayudante para que se quede con el bucle de lisent
    def start_helper(self):
        if not self.active:
            self.active = True
            self.helper = thr.Thread(target=self.lisent)
            self.helper.start()
            print("on")

#* Helper se quedara ejecutando este bucle infinitamente hasta que lo apaguemos colocando active en False
    def lisent(self):
        while self.active:
            self.keybord = keyboard.read_event()
            if self.keybord.event_type == 'down' and not self.keybord.name in self.list:
                self.list.append(self.keybord.name)
                self.keychaps.add(1)
                self.sound.play_sound(self.keybord.name)
            elif self.keybord.event_type == 'up' and self.keybord.name in self.list:
                self.list.remove(self.keybord.name)

#? Funciona para apagar a Helper
    def end_helper(self):
        self.active = False
        self.helper = None