class Wallet:
    def __init__(self, data_manager):
        self.data = data_manager
        self.balance = 0
    # Suma la Cantidad de Keychaps
    def add(self, cantidad):
        self.balance += cantidad
        self.data.update_keychaps(self.balance)
        self.data.save()
    # Resta la Cantidad de Keychaps
    def subtract(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            self.data.update_keychaps(self.balance)
            self.data.save()
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance