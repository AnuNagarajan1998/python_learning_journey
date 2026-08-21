from account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self,name,pin):
        super().__init__(name,pin)

    interest_rate = 5

    def calculate_interest(self):
        return ((self.balance * self.interest_rate)/100)