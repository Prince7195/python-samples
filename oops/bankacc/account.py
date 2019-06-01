class Account:

    def __init__(self, filePath):
        self.filePath = filePath
        with open(filePath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.commit()

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.commit()

    def commit(self):
        with open(self.filePath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    ''' This class generates an object. '''
    type = "Checking"

    def __init__(self, filePath, fee):
        Account.__init__(self, filePath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        self.commit()


checking = Checking("balance.txt", 1)
# print(checking.balance)
# checking.transfer(99)
# print(checking.balance)
print(checking.__doc__) # This class generates an object.