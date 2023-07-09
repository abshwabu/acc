class Account:
    def __init__(self,fpath):
        self.fpath = fpath
        with open(fpath,'r') as file:
            self.balance = int(file.read())
    

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount

    def commit(self):
        with open(self.fpath, 'w') as file:
            file.write(str(self.balance)) 


account = Account('balance.txt')
print(account.balance)
account.withdraw(200)
print(account.balance)
account.commit()