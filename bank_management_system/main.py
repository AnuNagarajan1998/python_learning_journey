from bank import *

bank = Bank()

while True:

    print("*" * 40)
    print(f"{'Welcome to our bank':^40}")
    print(f"{'1. Create Account':<10}")
    print(f"{'2. Login':<10}")
    print(f"{'3. Exit':<10}")
    print("*" * 40)

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter your name: ")
        pin = input("Enter your pin: ")
        acc_type = input("Enter account type (Savings/Current): ")

        account = bank.create_account(name, pin, acc_type)

        if isinstance(account, str):
            print(account)
        else:
            print("Account created successfully")
            print(f"Your account number is: {account}")

    elif choice == 2:

        account_no = int(input("Enter the account number: "))
        pin = input("Enter the pin: ")

        account = bank.login(account_no, pin)

        if account is None:
            print("Account Number or Pin is invalid")

        else:

            print("Login Successful")

            while True:

                print("*" * 40)
                print(f"{'Choose your task':^40}")
                print(f"{'1. Check Balance':<10}")
                print(f"{'2. Deposit':<10}")
                print(f"{'3. Withdraw':<10}")
                print(f"{'4. Calculate Interest':<10}")
                print(f"{'5. Mini Statement':<10}")
                print(f"{'6. Logout':<10}")
                print("*" * 40)

                task = int(input("Enter your choice: "))

                if task == 1:

                    print(account.check_balance())

                elif task == 2:

                    amount = float(input("Enter the amount to deposit: "))
                    account.deposit(amount)

                elif task == 3:

                    amount = float(input("Enter the amount to withdraw: "))
                    account.withdraw(amount)

                elif task == 4:
                    print(account.calculate_interest())

                elif task == 5:
                    account.mini_statement()

                elif task == 6:

                    print("Logged out successfully")
                    break

                else:

                    print("Invalid Choice")

    elif choice == 3:

        print("Thank you for using our bank")
        break

    else:

        print("Invalid Choice")