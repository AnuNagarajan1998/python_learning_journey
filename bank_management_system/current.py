from account import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self,name,pin):
        super().__init__(name,pin)

    interest_rate = 2

    def calculate_interest(self):
         return ((self.balance * self.interest_rate)/100)