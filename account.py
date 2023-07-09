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

class Checking(Account):
    def __init__(self,fpath,fee):
        Account.__init__(self,fpath)
        self.fee = fee
    def transfer(self,amount):
        self.balance = self.balance - amount-self.fee


checking = Checking('balance.txt',1)
print(checking.balance)
checking.withdraw(200)
print(checking.balance)
checking.commit()