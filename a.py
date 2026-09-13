import customtkinter as ctk
class Tienda(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.indice = 0

        self.geometry("300x600")
        self.title("Shop Keyboard")
        self.contenedor = ctk.CTkFrame(master=self, width=600, height=1000, fg_color="blue")
        self.contenedor.pack(pady=10)

        self.keybords = [
            {"nombre_keyboard": "Logitech", "precio_keyboard": 300, "nombre_mouse": "Logitech MK1", "precio_mouse": 205},
            {"nombre_keyboard": "Dragon", "precio_keyboard": 150, "nombre_mouse": "Razer M2", "precio_mouse": 192},
            {"nombre_keyboard": "Razer", "precio_keyboard": 200, "nombre_mouse": "Fantech M3", "precio_mouse": 500},
            {"nombre_keyboard": "Fantech", "precio_keyboard": 260, "nombre_mouse": "Fantech M3", "precio_mouse": 500}              
        ]

        self.frame_a_mostrar = self.keybords[self.indice : self.indice+3]
    def create_target(self):
        for i in self.frame_a_mostrar:
            print(i)
            tarjetas_keyboard = ctk.CTkFrame(
                master=self.contenedor,
                height=100
            )
            tarjetas_keyboard.pack(pady=10, padx=10, fill="x", side="left")
            name = ctk.CTkLabel(
                master=tarjetas_keyboard,
                text=i["nombre_keyboard"]
            )
            name.pack(pady=10)
            precio = ctk.CTkLabel(
                master=tarjetas_keyboard,
                text=i["precio_keyboard"]
            )
            precio.pack(pady=10)

            try_button = ctk.CTkButton(
                master=tarjetas_keyboard,
                text=f"Probar {i["nombre_keyboard"]}",
                command=lambda t=i: self.try_keyboard(t)
            )
            try_button.pack(pady=10)

            buy_keyboard = ctk.CTkButton(
                master=tarjetas_keyboard,
                text=f"Buy {i['nombre_keyboard']}",
                command=lambda h=i: self.buy_keyboard(h)
            )
            buy_keyboard.pack(pady=10)

    def try_keyboard(self, keyboard):
        print(f"Estas Probando Ahora mismo {keyboard["nombre_keyboard"]}")

    def buy_keyboard(self, keyboard):
        print(f"Acabas de comprar el {keyboard["nombre_keyboard"]}")

t = Tienda()
t.create_target()
t.mainloop()