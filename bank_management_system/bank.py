from saving import SavingsAccount
from current import CurrentAccount

class Bank:

    def __init__(self):
        self.accounts = []

    def create_account(self,name,pin,acc_type):

        if acc_type == "Savings":
            account = SavingsAccount(name,pin)
            self.accounts.append(account)

        elif acc_type == "Current":
            account = CurrentAccount(name,pin)
            self.accounts.append(account)

        else:
            return "Enter valid account type"

        return account.account_no

    def login(self,account_no,pin):
        if len(pin) == 4 and pin.isdigit():
            for account in self.accounts:
                if account.account_no == account_no and account.pin == pin:
                    return account
            return None
        else:
            return None

