class Account:
    def __init__(self,fpath):
        with open(fpath,'r') as file:
            self.balance = int(file.read())
    

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount


account = Account('balance.txt')
print(account.balance)
