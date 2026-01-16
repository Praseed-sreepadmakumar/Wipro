class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(self.balance)
        else:
            print("Amount Invalid")

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient Balance")

    def __del__(self):
        print("Account is deleted")

a1=BankAccount(1,5000)
a2=BankAccount(2,10000)
a1.withdraw(100)
a1.deposit(200)