from abc import ABC, abstractmethod
import random

class BankAccount(ABC):
    def __init__(self,name,pin):
        self.name = name
        self.pin = pin
        self.transactions = []
        self.balance = 0
        self.account_no = self.generate_account_number() # here the object calls its own method so use self

    #instance method beacuse it has self --> operates on an object
    def generate_account_number(self):
        return random.randint(100000, 999999)

    #declaring a private method

    def __add_transaction(self,transaction_type,amount):
        self.transactions.append({
            "type": transaction_type,
            "amount": amount
        }
        )
    def mini_statement(self):
        print("*" * 40)
        print(f"{'MINI STATEMENT':^40}")
        print("*" * 40)
        print(f"{'Transaction type':<10} {'AMOUNT':>12}")
        for transaction in self.transactions:
            print (f"{transaction['type']:<10} {transaction['amount']:>10}")

    def check_balance(self):
        if self.balance < 500:
            return "Insufficient balance"
        else:
            return self.balance

    def deposit(self,amount):

        self.balance += amount

        self.__add_transaction("CR", amount)

    def withdraw(self, amount):

        if(self.balance < 500):
            return  "Account with insufficient balance"
        elif(self.balance - amount < 500):
            return "Account balance runs low"
        else:
            self.balance -= amount
            self.__add_transaction("DR", amount)

    @abstractmethod
    def calculate_interest(self):
        pass
    