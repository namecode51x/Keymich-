# Import Archives
from economy.wallet import Wallet
from economy.cliclear import Clickear
from data.config_manager import DataManager
from sound.sound_manager import SoundManager
from gui.menu import Menu

#! Sistema de Guardado
dm = DataManager("src/data/user_data.json")
dm.change()

# Wallet sistema de Economia
wl = Wallet(dm)

# SoundManager
sd = SoundManager("assets/keyboard_sounds/Crimson", "assets/keyboard_sounds")
sd.search_sounds()
sd.search_keybords()
sd.load_sound_special()

#* Sistema de Clicker
cl = Clickear(wl, sd)
cl.start_helper()

# Menu System
Mn = Menu(sd, cl, wl)
sd.start_app()
Mn.mainloop()