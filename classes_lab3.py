class Account:
    def __init__(self, owner, bal):
        self.owner = owner
        self.bal = bal
    def deposit(self, dep):
        self.bal += dep
        print(f"{self.owner}, your balance: {self.bal}")
    def withdraw(self, wth):
        if self.bal - wth >= 0:
            self.bal -= wth
            print(f"{self.owner}, your balance: {self.bal}")
        else:
            print(f"{self.owner}, insufficient balance. You have {self.bal}")
p1 = Account("KBTU", 1000)
p2 = Account("Zukhra", 2000)

p1.deposit(100)
p1.withdraw(200)
p1.withdraw(1200)

p2.deposit(10000)
p2.withdraw(100)