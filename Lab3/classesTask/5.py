class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        if money > 0:
            self.balance += money
            print("New balance:", self.balance)
        else:
            print("The sum must be positive!")
        
    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient Funds")
        elif money > 0:
            self.balance -= money
            print("Remaining balance:", self.balance)
        else:
            print("Sum must be greater than 0!")
    
acc = Account("Nurdana", 150)

acc.deposit(100)
acc.withdraw(50)
acc.withdraw(250)
acc.withdraw(30)
acc.deposit(20)
acc.deposit(-35)
