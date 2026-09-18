# Simple Banking System

This project is a very simple beginner Python example for learning basic object-oriented programming.

## What the program does
- Creates a bank account
- Adds money to the account
- Takes money out of the account
- Checks that there is enough money before withdrawing
- Shows the balance
- Connects a customer to an account

## Beginner-friendly OOP concepts used
This project uses only simple OOP ideas:
- Classes: blueprints for creating objects
- Constructor: a special method used when creating an object
- Functions: actions the object can perform
- Variables: values stored in the object

## The classes in this project
### 1. Account
This class represents a bank account.
- It stores the account number
- It stores the balance
- It can deposit money
- It can withdraw money
- It can display the balance

### 2. Customer
This class represents a person using the bank.
- It stores the customer's name
- It keeps a reference to their account
- It can show customer information

### 3. Transaction
This class represents one bank action.
- It holds the account involved
- It holds the amount
- It holds the transaction type such as deposit or withdraw
- It runs the correct action automatically

## How the program works
1. A new account is created with an account number and starting balance.
2. A customer is created and linked to that account.
3. The program shows the starting account information.
4. A deposit is made.
5. A withdrawal is made.
6. The final balance is shown again.

## Files
- `banking_system.py` - main program

## How to run
Open a terminal and run:

```bash
python banking_system.py
```

## Example output
The program creates a customer called Alice, shows the balance, adds money, removes money, and then displays the final balance again.

## Notes
This is a small learning project designed to help beginners understand classes, objects, and simple methods in Python.
