import tkinter
import ctypes
import customtkinter as ctk
from tkinter import messagebox

class Menu(ctk.CTk):
    def __init__(self, sound_manager, clicker_system):
        super().__init__()
        self.sounds = sound_manager
        self.clicker_ = clicker_system
        self.geometry("600x500")
        self.title("keymich")
        self.icon = ("assets/icon_app/Keymich.ico")
        self.iconbitmap(self.icon)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Keymich.app.v1")
        self.menu = ctk.CTkOptionMenu(
            self, values=self.sounds.list_keybords, command=self.sounds.change_keyboard
            )
        self.menu.pack(pady=10)
        self.protocol("WM_DELETE_WINDOW", self.close_app)
    def close_app(self):
        self.clicker_.end_helper()
        self.destroy()