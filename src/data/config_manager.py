import json

class DataManager:
    def __init__(self, route):
        self.route = route

        #* Carga el archivo Json
    def change(self):
        with open(self.route, 'r') as archive:
            self.archive_read = json.load(archive)

 #* Sobre Escribe el archivo Json
    def save(self):
        with open(self.route, 'w') as archive_write:
            json.dump(self.archive_read, archive_write)

    def get_keychaps(self):
        value = self.archive_read.get("keychaps")
        return value

    def update_keychaps(self, amount):
        self.archive_read["keychaps"] = amount