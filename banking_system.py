# Simple banking system example
# This file shows basic OOP in Python.
# We use classes, variables, constructor methods, and functions.


class Account:
    # The constructor sets up a new account with an account number and balance.
    def __init__(self, account_number, balance=0):
        # These variables store the account information.
        self.account_number = account_number
        self.balance = balance

    # This function adds money to the account.
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    # This function removes money from the account if there is enough money.
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient funds!")

    # This function shows the current account information.
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")


class Customer:
    # The constructor creates a customer and links them to an account.
    def __init__(self, name, account):
        self.name = name
        self.account = account

    # This function prints the customer name and account balance.
    def display_customer_info(self):
        print(f"Customer Name: {self.name}")
        self.account.display_balance()


class Transaction:
    # This class handles a deposit or withdrawal for an account.
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

        # Run the transaction immediately when the object is created.
        self.process_transaction()

    # This function checks what type of transaction should happen.
    def process_transaction(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")


if __name__ == "__main__":
    # Create a new account and customer.
    account1 = Account(197877, 100)
    customer1 = Customer(name="Alice", account=account1)

    # Show the starting balance.
    customer1.display_customer_info()

    # Make a deposit and a withdrawal.
    Transaction(account1, 50, "deposit")
    Transaction(account1, 30, "withdraw")

    # Show the final balance.
    customer1.display_customer_info()