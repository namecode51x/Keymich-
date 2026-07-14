class Wallet:
    def __init__(self):
        self.balance = 0

    def add(self, cantidad):
        self.balance += cantidad
    
    def subtract(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance