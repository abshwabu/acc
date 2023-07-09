class Account:
    def __init__(self,path):
        with open(path,'r') as file:
            self.balance = int(file.read)
    

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount