class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        print(f"Deposited: {deposit} tenge. New balance: {self.balance} tenge.")

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            print(f"Withdrew {money} tenge. New balance: {self.balance} tenge")
        else:
            print("NOT ENOUGH MONEY!!!")
human = Account("Damir", 600)
human.withdraw(1000)
human.deposit(1000)
human.withdraw(1000)
