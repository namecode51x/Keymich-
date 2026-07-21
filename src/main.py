from economy.wallet import Wallet
from economy.cliclear import Clickear
from data.config_manager import DataManager
from sound.sound_manager import SoundManager

#! Sistema de Guardado
dm = DataManager("src/data/user_data.json")
dm.change()

# Wallet sistema de Economia
wl = Wallet(dm)

# SoundManager
sd = SoundManager("assets/keyboard_sounds/keyboardRed")
sd.search_sounds()
sd.load_sound_special()

#* Sistema de Clicker
cl = Clickear(wl, sd)
cl.start_helper()