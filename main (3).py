class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("Deposited ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdrawn ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print("Account balance for {} (Account #{}): ₹{}".format(
            self.__account_holder_name, self.__account_number, self.__account_balance))

# Create an instance of BankAccount
account = BankAccount(account_number="123456789", account_holder_name="mushbiqa", initial_balance=5000.0)
account.display_balance()  # Display initial balance
account.deposit(500.0)     # Deposit ₹500
account.withdraw(200.0)    # Withdraw ₹200
account.display_balance()  # Display updated balance
