import tkinter
import ctypes
import pystray
import threading as thr
import customtkinter as ctk

from turtle import left, right
from tkinter import messagebox
from PIL import Image
from pygame import image

from economy import wallet

class Menu(ctk.CTk):
    def __init__(self, sound_manager, clicker_system, wallet_):
        super().__init__()

        # Class Sound Manager
        self.sound_manager = sound_manager
        self.keybord_current.a = self.sound_manager

        # Class Clicker
        self.clicker_ = clicker_system

        # Class Wallet
        self.wallet = wallet_
        self.counter = ctk.IntVar()
        self.wallet.counter = self.counter
        self.counter.set(self.wallet.get_balance())

        #* INDICE DEL Carrucel
        self.indice = 0

        # Indice del Carrucel activo
        self.tarjetas_a_mostrar = self.sound_manager.list_keybords[self.indice : self.indice+3]

        #? ROUTE KEYBOARDS
        self.route_keyboards = "assets/keyboard_sounds"
        # Route Icon
        self.icon_keychaps = "assets/keychaps_icon/Keychaps.png"
        self.icon_keymich = "assets/icon_app/Keymich.png"

        self.icons_keybords = "assets/icons_keyboards/icon.png"

        #* Charge Icon keychaps
        self.icon_keychaps_change = ctk.CTkImage(
            light_image=Image.open(self.icon_keychaps), 
            dark_image=Image.open(self.icon_keychaps),
            size=(75, 60)
        )

        # Charge Logo Keymich
        self.logo = ctk.CTkImage(
            light_image=Image.open(self.icon_keymich),
            dark_image=Image.open(self.icon_keymich),
            size=(120, 120)
        )

        self.icon_keyboards = ctk.CTkImage(
            light_image=Image.open(self.icons_keybords),
            dark_image=Image.open(self.icons_keybords),
            size=(250, 250)
        )


        #? Windows

         # Resolucion Of windows
        self.geometry("600x500")

          # Name of windows
        self.title("keymich")

           # Icon of Windows
        self.icon = ("assets/icon_app/Keymich.ico")
        self.iconbitmap(self.icon)

            # Icon Bar Windows
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Keymich.app.v1")

        #* Frame Superior
        self.frame_superior = ctk.CTkFrame(master=self, height=80)

        #? Mini Frame Superior Derecho
        self.mini_frame_superior_derecho = ctk.CTkFrame(master=self.frame_superior, fg_color="transparent")

        # Mini Frame Superior Izquierdo
        self.mini_frame_superior_izquierdo = ctk.CTkFrame(master=self.frame_superior, fg_color="transparent")

        #! Frame Derecho
        self.frame_derecho = ctk.CTkFrame(master=self, width=30)

        self.titule_my_packs = ctk.CTkLabel(master=self.frame_derecho, text="My Packs:", width=180)
        
        # Frame Central Keyboards
        self.frame_central_keyboards = ctk.CTkFrame(master=self,
        corner_radius=15,
        border_width=2,
        border_color="black"
        )

        # Name Keymich in Windows
        self.titule_in_windows = ctk.CTkLabel(
            master=self.frame_superior, text="Keymich", image=self.logo,
             compound="left", font=("Ariel", 16)
            )

        #? Icon Slider Volumen
        self.icon_volumen_slider = ctk.CTkLabel(
            master=self.mini_frame_superior_derecho,
            text="🔊"
        )

        # Slider Volume
        self.sound_slider = ctk.CTkSlider(
            master=self.mini_frame_superior_derecho,
            from_=0,
            to=1,
            command=self.sound_manager.volumen_change
        )

        # Counter Keychaps
        self.counter_keychaps = ctk.CTkLabel(
            textvariable=self.counter,
            master=self.mini_frame_superior_izquierdo,
            image=self.icon_keychaps_change,
            compound="left"
        )

        #? TITULE KEYCHAPS
        self.titule_keychaps = ctk.CTkLabel(
            master=self.mini_frame_superior_izquierdo,
            text="Keychaps"
        )

        # Options Keyboards
        self.menu_keybords = ctk.CTkOptionMenu(
            self, values=self.sound_manager.list_keybords, command=self.sound_manager.change_keyboard
            )

    def tarjetas(self, name_keyboard, price_keyboard, image_keyboard):
        # RECORRE TODAS LAS TARJETAS VISIBLES Y HACE QUE SE VEAN
     for t in self.tarjetas_a_mostrar:
        change_icon_keyboard = ctk.CTkImage(
            light_image=Image.open(self.route_keyboards + name_keyboard + ext),
            dark_image=Image.open(self.route_keyboards + name_keyboard + ext),
            size=(100, 100)
        )
        ext = ".png"

        #! TARJETAS DE LOS TECLADOS
        tarjeta_keyboard = ctk.CTkFrame(
            master=self.frame_central_keyboards,
            border_width=2
        )
        tarjeta_keyboard.pack(pady=10, padx=10, fill="x", side="left")

        # NOMBRE DEL KEYBOARD
        name_tarjeta = ctk.CTkLabel(
            master=tarjeta_keyboard,
            text=name_keyboard,
        )

        # Imagen Keyboard
        icon_keyboard = ctk.CTkLabel(
            master=tarjeta_keyboard,
            image=image_keyboard
        )

        # Precio del Keyboard
        price_keyboard = ctk.CTkLabel(
            master=tarjeta_keyboard,
            text=""
        )

        #? PRUEBA EL TECLADO ESCUCHANDO SU SONIDO X 30 SEGUNDO
        prueba_button = ctk.CTkButton(
            master=tarjeta_keyboard,
            text="Prueba",
            corner_radius=15,
            command=""
        )

        #* COMPRAR EL TECLADO
        buy_keyboard = ctk.CTkButton(
            master=self.tarjeta_keyboard,
            text="Buy",
            corner_radius=15,
            command=""
        )

    def empaquetar(self):
        #* Columnas COnfigure
        self.frame_superior.columnconfigure(0, weight=1)
        self.frame_superior.columnconfigure(1, weight=1)
        self.frame_superior.columnconfigure(2, weight=1)

        # Empaquetar
         #* Frames
        self.frame_superior.pack(side="top", fill="x")
        self.mini_frame_superior_derecho.grid(row=0, column=2, sticky="e")
        self.mini_frame_superior_izquierdo.grid(row=0, column=0, sticky="w")

        self.frame_derecho.pack(side="right", fill="y", padx=(0))
        self.titule_my_packs.pack(side="top")
        self.titule_in_windows.grid(row=0, column=1, sticky="", padx=10)
        self.menu_keybords.pack(pady=10)
        self.counter_keychaps.pack(side="left")
        self.titule_keychaps.pack(side="right", padx=5)
        
        #? Volumen Pack
        self.icon_volumen_slider.pack(side="left")
        self.sound_slider.pack(side="left")
        
        #! Close Windows
        self.protocol("WM_DELETE_WINDOW", self.close_app)

    def create_tarjet(self):
        for i in self.sound_manager.search_keybords:
            self.tarjetas()

    # DEJAR APLIACION EN SEGUNDO PLANO
    def background(self):
        mini_menu = pystray.Menu(
            pystray.MenuItem('Open', self.open_windows),
            pystray.MenuItem('Close', self.close_windows)
        )
        Icon = pystray.Icon("Keymich", Image.open(self.icon_keymich), "Keymich", menu=mini_menu).run()

    def open_windows(self):
        self.after(0, self.deiconify)

    def close_windows(self):
        self.after(0, self.destroy)
        self.clicker_.end_helper()
            
    def close_app(self):
        self.withdraw()
        self.helper = thr.Thread(target=self.background)
        self.helper.start()
        print("on")