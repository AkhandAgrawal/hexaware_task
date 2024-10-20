# Banking System

# Control Structure

# Task 1: Conditional Statements

# In a bank, you have been given the task is to create a program that checks if a customer is eligible for 
# a loan based on their credit score and income. The eligibility criteria are as follows:
# • Credit Score must be above 700.
# • Annual Income must be at least $50,000.
# Tasks:
# 1. Write a program that takes the customer's credit score and annual income as input.
# 2. Use conditional statements (if-else) to determine if the customer is eligible for a loan.
# 3. Display an appropriate message based on eligibility.


# credit_score = int(input("Enter your credit score: "))
# annual_income = float(input("Enter your annual income: "))

# if credit_score > 700 and annual_income >= 50000:
#     print("Congratulations! You are eligible for the loan.")
# else:
#     print("Sorry, you are not eligible for the loan.")

# =================================================================================================

# Task 2: Nested Conditional Statements
# Create a program that simulates an ATM transaction. Display options such as "Check Balance," 
# "Withdraw," "Deposit,". Ask the user to enter their current balance and the amount they want to 
# withdraw or deposit. Implement checks to ensure that the withdrawal amount is not greater than the 
# available balance and that the withdrawal amount is in multiples of 100 or 500. Display appropriate 
# messages for success or failure.

# print("Options:")
# print("1. Check Balance")
# print("2. Withdraw")
# print("3. Deposit")
# option = int(input("Select an option 1/2/3: "))
# current_balance = float(input("Enter your current balance: "))

# if option == 1:
#     print("Your current balance is: {}".format(current_balance))

# elif option == 2:
#     withdraw_amount = float(input("Enter the amount to withdraw: "))
#     if withdraw_amount > current_balance:
#         print("Insufficient balance. Withdrawal failed.")
#     elif withdraw_amount % 100 != 0 and withdraw_amount % 500 != 0:
#         print("Withdrawal amount must be in multiples of 100 or 500.")
#     else:
#         current_balance -= withdraw_amount
#         print("Withdrawal successful. Your new balance is: {}".format(current_balance))

# elif option == 3:
#     deposit_amount = float(input("Enter the amount to deposit: "))
#     current_balance += deposit_amount
#     print("Deposit successful. Your new balance is: {}".format(current_balance))

# else:
#     print("Invalid option. Please select 1, 2, or 3.")


# =========================================================================================

# Task 3: Loop Structures
# You are responsible for calculating compound interest on savings accounts for bank customers. You 
# need to calculate the future balance for each customer's savings account after a certain number of years.
# Tasks:
# 1. Create a program that calculates the future balance of a savings account.
# 2. Use a loop structure (e.g., for loop) to calculate the balance for multiple customers.
# 3. Prompt the user to enter the initial balance, annual interest rate, and the number of years.
# 4. Calculate the future balance using the formula: 
# future_balance = initial_balance * (1 + annual_interest_rate/100)^years.
# 5. Display the future balance for each customer.


# num_customers = int(input("Enter the number of customers: "))

# for i in range(num_customers):
#     initial_balance = float(input("Enter the initial balance for customer {}: ".format(i + 1)))
#     annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
#     years = int(input("Enter the number of years: "))
    
#     future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years
#     print("Future balance for customer {}: ${:.2f}".format(i + 1, future_balance))



# ===============================================================================================================


# Task 4: Looping, Array and Data Validation
# You are tasked with creating a program that allows bank customers to check their account balances. 
# The program should handle multiple customer accounts, and the customer should be able to enter their 
# account number, balance to check the balance.
# Tasks:
# 1. Create a Python program that simulates a bank with multiple customer accounts.
# 2. Use a loop (e.g., while loop) to repeatedly ask the user for their account number and 
# balance until they enter a valid account number.
# 3. Validate the account number entered by the user.
# 4. If the account number is valid, display the account balance. If not, ask the user to try again.

# accounts = {
#     "1001": 5000.00,
#     "1002": 10000.00,
#     "1003": 15000.00,
#     "1004": 20000.00,
#     "1005": 25000.00
# }
# while True:
#     account_number = input("Enter your account number (or type 'q' to quit): ")
#     if account_number == 'q':
#         print("Exiting the program.")
#         break
#     if account_number in accounts:
#         balance = accounts[account_number]
#         print("Your account balance is: ${:.2f}".format(balance))
#     else:
#         print("Invalid account number. Please try again.")


# ====================================================================================================

# Task 5: Password Validation
# Write a program that prompts the user to create a password for their bank account. Implement if 
# conditions to validate the password according to these rules:
# • The password must be at least 8 characters long.
# • It must contain at least one uppercase letter.
# • It must contain at least one digit.
# • Display appropriate messages to indicate whether their password is valid or not.


# while True:
#     password = input("Create a password for your bank account: ")
#     if len(password) < 8:
#         print("Password must be at least 8 characters long.")
#     elif not any(char.isupper() for char in password):
#         print("Password must contain at least one uppercase letter.")
#     elif not any(char.isdigit() for char in password):
#         print("Password must contain at least one digit.")
#     else:
#         print("Password is valid!")
#         break 


# ============================================================================================================

# Task 6: Password Validation
# Create a program that maintains a list of bank transactions (deposits and withdrawals) for a customer. 
# Use a while loop to allow the user to keep adding transactions until they choose to exit. Display the 
# transaction history upon exit using looping statements


# transactions = []
# while True:
#     transaction_type = input("Enter 'deposit' or 'withdrawal' (or 'q' to quit): ")
#     if transaction_type == 'q':
#         break
#     amount = float(input("Enter the amount: "))
#     transactions.append((transaction_type, amount))

# print("Transaction History:")
# i = 1
# for transaction in transactions:
#     print("{}. {} of {:.2f}".format(i, transaction[0], transaction[1]))
#     i += 1

# =============================================================================================


# OOPS, Collections and Exception Handling

# Task 7: Class & Object

# 1. Create a `Customer` class with the following confidential attributes:
# • Attributes
# o Customer ID
# o First Name
# o Last Name
# o Email Address
# o Phone Number
# o Address
# • Constructor and Methods
# o Implement default constructors and overload the constructor with Customer 
# attributes, generate getter and setter, (print all information of attribute) methods for the attributes.


# class Customer:
#     def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address=None):
#         self.customer_id = customer_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone = phone
#         self.address = address

#     def get_customer_info(self):
#         return "ID: {}\nName: {} {}\nEmail: {}\nPhone: {}\nAddress: {}".format(
#             self.customer_id, self.first_name, self.last_name, self.email, self.phone, self.address)

#     def set_customer_info(self, customer_id, first_name, last_name, email, phone, address):
#         self.customer_id = customer_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone = phone
#         self.address = address

# customer = Customer() 
# customer.set_customer_info(101, "Ram", "Sharma", "ramsharma@gmail.com", "8765454310", "Mumbai")
# print(customer.get_customer_info())



# 2. Create an `Account` class with the following confidential attributes:
# • Attributes
# o Account Number
# o Account Type (e.g., Savings, Current)
# o Account Balance
# • Constructor and Methods
# o Implement default constructors and overload the constructor with Account attributes,
# o Generate getter and setter, (print all information of attribute) methods for the attributes.
# o Add methods to the `Account` class to allow deposits and withdrawals.
# - deposit(amount: float): Deposit the specified amount into the account.
# - withdraw(amount: float): Withdraw the specified amount from the account. 
# withdraw amount only if there is sufficient fund else display insufficient balance.
# - calculate_interest(): method for calculating interest amount for the available 
# balance. interest rate is fixed to 4.5%
# # • Create a Bank class to represent the banking system. Perform the following operation in main method:
# # o create object for account class by calling parameter constructor.
# # o deposit(amount: float): Deposit the specified amount into the account.
# # o withdraw(amount: float): Withdraw the specified amount from the account.
# # o calculate_interest(): Calculate and add interest to the account balance for savings accounts.

# class Account:
#     def __init__(self, account_number=None, account_type=None, balance=0.0):
#         self.account_number = account_number
#         self.account_type = account_type
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print("Deposited ${:.2f}. Current balance: ${:.2f}".format(amount, self.balance))
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn ${:.2f}. Current balance: ${:.2f}".format(amount, self.balance))
#     def calculate_interest(self):
#             interest_rate = 4.5 / 100
#             interest = self.balance * interest_rate
#             self.balance += interest
#             print("Interest of {:.2f} added. New Balance: {:.2f}".format(interest, self.balance))
#     def get_account_info(self):
#         return "Account Number: {}\nAccount Type: {}\nBalance: ${:.2f}".format(self.account_number, self.account_type, self.balance)


# class Bank:
#     def main(self):
#         account = Account(1234567890, "Savings", 500.00)
#         print(account.get_account_info())
#         account.deposit(200.00)
#         account.withdraw(100.00)
#         account.calculate_interest()
#         print(account.get_account_info())

# bank = Bank()
# bank.main()

# ===============================================================================================================================


# Task 8: Inheritance and polymorphism
# 1. Overload the deposit and withdraw methods in Account class as mentioned below.
# • deposit(amount: float): Deposit the specified amount into the account.
# • withdraw(amount: float): Withdraw the specified amount from the account. withdraw 
# amount only if there is sufficient fund else display insufficient balance.
# • deposit(amount: int): Deposit the specified amount into the account.
# • withdraw(amount: int): Withdraw the specified amount from the account. withdraw 
# amount only if there is sufficient fund else display insufficient balance.
# • deposit(amount: double): Deposit the specified amount into the account.
# • withdraw(amount: double): Withdraw the specified amount from the account. withdraw 
# amount only if there is sufficient fund else display insufficient balance.

# class Account:
#     def __init__(self, account_number=None, account_type=None, balance=0.0):
#         self.account_number = account_number
#         self.account_type = account_type
#         self.balance = balance

#     def deposit(self, amount):
#         if isinstance(amount, (int, float)) and amount > 0:
#             self.balance += amount
#             print("Deposited ${:.2f}. Current balance: ${:.2f}".format(amount, self.balance))
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         if isinstance(amount, (int, float)) and amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print("Withdrawn ${:.2f}. Current balance: ${:.2f}".format(amount, self.balance))
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Invalid withdrawal amount.")

#     def calculate_interest(self):
#         raise NotImplementedError("This method should be overridden in subclasses.")

#     def get_account_info(self):
#         return "Account Number: {}\nAccount Type: {}\nBalance: ${:.2f}".format(self.account_number, self.account_type, self.balance)



# 2. Create Subclasses for Specific Account Types
# • Create subclasses for specific account types (e.g., `SavingsAccount`, `CurrentAccount`) 
# that inherit from the `Account` class.
# o SavingsAccount: A savings account that includes an additional attribute for 
# interest rate. override the calculate_interest() from Account class method to 
# calculate interest based on the balance and interest rate.
# o CurrentAccount: A current account that includes an additional attribute 
# overdraftLimit. A current account with no interest. Implement the withdraw() 
# method to allow overdraft up to a certain limit (configure a constant for the 
# overdraft limit).

# class SavingsAccount(Account):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, "Savings", balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * (self.interest_rate / 100)
#         self.balance += interest
#         print("Interest of ${:.2f} added. New balance: ${:.2f}".format(interest, self.balance))


# class CurrentAccount(Account):
#     OVERDRAFT_LIMIT = 500.00

#     def __init__(self, account_number, balance):
#         super().__init__(account_number, "Current", balance)

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance + CurrentAccount.OVERDRAFT_LIMIT:
#             self.balance -= amount
#             print("Withdrawn ${:.2f}. Current balance: ${:.2f}".format(amount, self.balance))
#         else:
#             print("Withdrawal exceeds overdraft limit.")



# 3. Create a Bank class to represent the banking system. Perform the following operation in main 
# method:
# • Display menu for user to create object for account class by calling parameter 
# constructor. Menu should display options `SavingsAccount` and `CurrentAccount`. user 
# can choose any one option to create account. use switch case for implementation.
# • deposit(amount: float): Deposit the specified amount into the account.
# • withdraw(amount: float): Withdraw the specified amount from the account. For saving 
# account withdraw amount only if there is sufficient fund else display insufficient balance. 
# For Current Account withdraw limit can exceed the available balance and should not 
# exceed the overdraft limit.
# • calculate_interest(): Calculate and add interest to the account balance for savings 
# accounts.

# class Bank:
#     def main(self):
#         print("Welcome to the Bank!")
#         print("1. Create Savings Account")
#         print("2. Create Current Account")
#         choice = int(input("Choose account type (1 or 2): "))

#         account_number = input("Enter Account Number: ")
#         initial_balance = float(input("Enter Initial Balance: "))

#         if choice == 1:
#             interest_rate = float(input("Enter Interest Rate (in %): "))
#             account = SavingsAccount(account_number, initial_balance, interest_rate)
#         elif choice == 2:
#             account = CurrentAccount(account_number, initial_balance)
#         else:
#             print("Invalid choice.")
#             return

#         while True:
#             print("\nMenu:")
#             print("1. Deposit")
#             print("2. Withdraw")
#             print("3. Calculate Interest (Savings Account Only)")
#             print("4. View Account Info")
#             print("5. Exit")
#             option = int(input("Choose an option: "))
#             if option == 1:
#                 amount = float(input("Enter amount to deposit: "))
#                 account.deposit(amount)
#             elif option == 2:
#                 amount = float(input("Enter amount to withdraw: "))
#                 account.withdraw(amount)
#             elif option == 3:
#                 if isinstance(account, SavingsAccount):
#                     account.calculate_interest()
#                 else:
#                     print("Interest calculation is only available for savings accounts.")
#             elif option == 4:
#                 print(account.get_account_info())
#             elif option == 5:
#                 print("Exiting the system.")
#                 break
#             else:
#                 print("Invalid option or action not allowed.")


# bank = Bank()
# bank.main()



# ==================================================================================================================


# Task 9: Abstraction

# 1. Create an abstract class BankAccount that represents a generic bank account. It should include 
# the following attributes and methods:
# • Attributes:
# o Account number.
# o Customer name.
# o Balance.
# • Constructors:
# o Implement default constructors and overload the constructor with Account 
# attributes, generate getter and setter, print all information of attribute methods 
# for the attributes.
# • Abstract methods:
# o deposit(amount: float): Deposit the specified amount into the account.
# o withdraw(amount: float): Withdraw the specified amount from the account 
# (implement error handling for insufficient funds).
# o calculate_interest(): Abstract method for calculating interest.

# from abc import ABC, abstractmethod

# class BankAccount(ABC):
#     def __init__(self, account_number=None, customer_name=None, balance=0.0):
#         self.account_number = account_number
#         self.customer_name = customer_name
#         self.balance = balance

#     def get_account_number(self):
#         return self.account_number

#     def set_account_number(self, account_number):
#         self.account_number = account_number

#     def get_customer_name(self):
#         return self.customer_name

#     def set_customer_name(self, customer_name):
#         self.customer_name = customer_name

#     def get_balance(self):
#         return self.balance

#     def set_balance(self, balance):
#         self.balance = balance

#     def print_account_info(self):
#         print(f"Account Number: {self.account_number}")
#         print(f"Customer Name: {self.customer_name}")
#         print(f"Balance: ${self.balance:.2f}")

#     @abstractmethod
#     def deposit(self, amount: float):
#         pass

#     @abstractmethod
#     def withdraw(self, amount: float):
#         pass

#     @abstractmethod
#     def calculate_interest(self):
#         pass



# 2. Create two concrete classes that inherit from BankAccount:
# • SavingsAccount: A savings account that includes an additional attribute for interest rate. 
# Implement the calculate_interest() method to calculate interest based on the balance 
# and interest rate.
# • CurrentAccount: A current account with no interest. Implement the withdraw() method 
# to allow overdraft up to a certain limit (configure a constant for the overdraft limit).

# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, customer_name, balance, interest_rate):
#         super().__init__(account_number, customer_name, balance)
#         self.interest_rate = interest_rate

#     def deposit(self, amount: float):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount:.2f}. Current balance: ${self.balance:.2f}")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount: float):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Withdrawn ${amount:.2f}. Current balance: ${self.balance:.2f}")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Invalid withdrawal amount.")

#     def calculate_interest(self):
#         interest = self.balance * (self.interest_rate / 100)
#         self.balance += interest
#         print(f"Interest of ${interest:.2f} added. New balance: ${self.balance:.2f}")


# class CurrentAccount(BankAccount):
#     OVERDRAFT_LIMIT = 500.0
#     def __init__(self, account_number, customer_name, balance):
#         super().__init__(account_number, customer_name, balance)

#     def deposit(self, amount: float):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount:.2f}. Current balance: ${self.balance:.2f}")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount: float):
#         if amount > 0:
#             if amount <= self.balance + CurrentAccount.OVERDRAFT_LIMIT:
#                 self.balance -= amount
#                 print(f"Withdrawn ${amount:.2f}. Current balance: ${self.balance:.2f}")
#             else:
#                 print("Withdrawal exceeds overdraft limit.")
#         else:
#             print("Invalid withdrawal amount.")

#     def calculate_interest(self):
#         print("No interest for Current Account.")



# 3. Create a Bank class to represent the banking system. Perform the following operation in main 
# method:
# • Display menu for user to create object for account class by calling parameter 
# constructor. Menu should display options `SavingsAccount` and `CurrentAccount`. user 
# can choose any one option to create account. use switch case for implementation.
# create_account should display sub menu to choose type of accounts.
# o Hint: Account acc = new SavingsAccount(); or Account acc = new 
# CurrentAccount();
# • deposit(amount: float): Deposit the specified amount into the account.
# • withdraw(amount: float): Withdraw the specified amount from the account. For saving
# account withdraw amount only if there is sufficient fund else display insufficient balance. 
# For Current Account withdraw limit can exceed the available balance and should not 
# exceed the overdraft limit.
# • calculate_interest(): Calculate and add interest to the account balance for savings 
# accounts.

# class Bank:
#     def main(self):
#         print("Welcome to the Bank!")
#         print("1. Create Savings Account")
#         print("2. Create Current Account")
#         choice = int(input("Choose account type (1 or 2): "))

#         account_number = input("Enter Account Number: ")
#         customer_name = input("Enter Customer Name: ")
#         initial_balance = float(input("Enter Initial Balance: "))

#         if choice == 1:
#             interest_rate = float(input("Enter Interest Rate (in %): "))
#             account = SavingsAccount(account_number, customer_name, initial_balance, interest_rate)
#         elif choice == 2:
#             account = CurrentAccount(account_number, customer_name, initial_balance)
#         else:
#             print("Invalid choice.")
#             return

#         while True:
#             print("\nMenu:")
#             print("1. Deposit")
#             print("2. Withdraw")
#             print("3. Calculate Interest (Savings Account Only)")
#             print("4. View Account Info")
#             print("5. Exit")
#             option = int(input("Choose an option: "))

#             if option == 1:
#                 amount = float(input("Enter amount to deposit: "))
#                 account.deposit(amount)
#             elif option == 2:
#                 amount = float(input("Enter amount to withdraw: "))
#                 account.withdraw(amount)
#             elif option == 3:
#                 if isinstance(account, SavingsAccount):
#                     account.calculate_interest()
#                 else:
#                     print("Interest calculation is only available for savings accounts.")
#             elif option == 4:
#                 account.print_account_info()
#             elif option == 5:
#                 print("Exiting the system.")
#                 break
#             else:
#                 print("Invalid option or action not allowed.")

# bank = Bank()
# bank.main()




# =====================================================================================================


# Task 10: Has A Relation / Association

# 1. Create a `Customer` class with the following attributes:
# • Customer ID
# • First Name
# • Last Name
# • Email Address (validate with valid email address)
# • Phone Number (Validate 10-digit phone number)
# • Address
# • Methods and Constructor:
# o Implement default constructors and overload the constructor with Account 
# attributes, generate getter, setter, print all information of attribute) methods for 
# the attributes.

# import re
# class Customer:
#     def __init__(self, customer_id=None, first_name="", last_name="", email="", phone="", address=""):
#         self.customer_id = customer_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = self.validate_email(email)
#         self.phone = self.validate_phone(phone)
#         self.address = address

#     def validate_email(self, email):
#         pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
#         if re.match(pattern, email):
#             return email
#         else:
#             return None  

#     def validate_phone(self, phone):
#         pattern = r"^\d{10}$"
#         if re.match(pattern, phone):
#             return phone
#         else:
#             return None  

#     def print_info(self):
#         print(f"Customer ID: {self.customer_id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\n"
#               f"Email: {self.email}\nPhone: {self.phone}\nAddress: {self.address}\n")


# 2. Create an `Account` class with the following attributes:
# • Account Number (a unique identifier).
# • Account Type (e.g., Savings, Current)
# • Account Balance
# • Customer (the customer who owns the account)
# • Methods and Constructor:
# o Implement default constructors and overload the constructor with Account 
# attributes, generate getter, setter, (print all information of attribute) methods for 
# the attributes.

# class Account:
#     account_counter = 1001 

#     def __init__(self, account_type="", balance=0.0, customer=None):
#         self.account_number = Account.account_counter
#         Account.account_counter += 1
#         self.account_type = account_type
#         self.balance = balance
#         self.customer = customer

#     def print_info(self):
#         print(f"Account Number: {self.account_number}\nAccount Type: {self.account_type}\n"
#               f"Account Balance: ${self.balance:.2f}\nCustomer Details:")
#         self.customer.print_info()


# Create a Bank Class and must have following requirements:
# 1. Create a Bank class to represent the banking system. It should have the following methods:
# • create_account(Customer customer, long accNo, String accType, float balance): Create 
# a new bank account for the given customer with the initial balance.
# • get_account_balance(account_number: long): Retrieve the balance of an account given 
# its account number. should return the current balance of account.
# • deposit(account_number: long, amount: float): Deposit the specified amount into the 
# account. Should return the current balance of account.
# • withdraw(account_number: long, amount: float): Withdraw the specified amount from 
# the account. Should return the current balance of account.
# • transfer(from_account_number: long, to_account_number: int, amount: float): 
# Transfer money from one account to another.
# • getAccountDetails(account_number: long): Should return the account and customer 
# details.

# 2. Ensure that account numbers are automatically generated when an account is created, starting 
# from 1001 and incrementing for each new account.

# class Bank:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self, customer, account_type, balance):
#         account = Account(account_type, balance, customer)
#         self.accounts[account.account_number] = account
#         print(f"Account created successfully with Account Number: {account.account_number}")

#     def get_account_balance(self, account_number):
#         account = self.accounts.get(account_number)
#         if account:
#             return account.balance
#         return None

#     def deposit(self, account_number, amount):
#         account = self.accounts.get(account_number)
#         if account and amount > 0:
#             account.balance += amount
#             return account.balance
#         return None

#     def withdraw(self, account_number, amount):
#         account = self.accounts.get(account_number)
#         if account and amount > 0:
#             if account.balance >= amount:
#                 account.balance -= amount
#                 return account.balance
#             else:
#                 print("Insufficient balance.")
#                 return account.balance
#         return None

#     def transfer(self, from_account_number, to_account_number, amount):
#         from_account = self.accounts.get(from_account_number)
#         to_account = self.accounts.get(to_account_number)
#         if from_account and to_account and amount > 0:
#             if from_account.balance >= amount:
#                 from_account.balance -= amount
#                 to_account.balance += amount
#                 print(f"Transferred ${amount:.2f} from Account {from_account_number} to Account {to_account_number}.")
#                 return from_account.balance
#             else:
#                 print("Insufficient balance in the source account.")
#                 return None
#         return None

#     def get_account_details(self, account_number):
#         account = self.accounts.get(account_number)
#         if account:
#             account.print_info()
#         else:
#             print("Account not found.")


# 3. Create a BankApp class with a main method to simulate the banking system. Allow the user to 
# interact with the system by entering commands such as "create_account", "deposit", 
# "withdraw", "get_balance", "transfer", "getAccountDetails" and "exit." create_account should 
# display sub menu to choose type of accounts and repeat this operation until user exit.

# class BankApp:
#     def __init__(self):
#         self.bank = Bank()

#     def display_menu(self):
#         print("\n--- Banking System Menu ---")
#         print("1. Create Account")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Get Balance")
#         print("5. Transfer")
#         print("6. Get Account Details")
#         print("7. Exit")
#         print("---------------------------")

#     def main(self):
#         while True:
#             self.display_menu()
#             command = input("Enter the number of the command you want to execute: ").strip()

#             if command == "1":
#                 first_name = input("Enter First Name: ")
#                 last_name = input("Enter Last Name: ")
#                 email = input("Enter Email: ")
#                 phone = input("Enter Phone Number: ")
#                 address = input("Enter Address: ")
#                 customer = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address)
#                 if customer.email is None:
#                     print("Invalid email address.")
#                     continue
#                 if customer.phone is None:
#                     print("Invalid phone number. It must be 10 digits.")
#                     continue
#                 account_type = input("Choose Account Type (Savings or Current): ").strip().lower()
#                 try:
#                     initial_balance = float(input("Enter Initial Balance: "))
#                     self.bank.create_account(customer, account_type.capitalize(), initial_balance)
#                     print("Account created successfully.")
#                 except ValueError:
#                     print("Invalid balance. Please enter a valid number.")

#             elif command == "2":
#                 try:
#                     account_number = int(input("Enter Account Number: "))
#                     amount = float(input("Enter Deposit Amount: "))
#                     new_balance = self.bank.deposit(account_number, amount)
#                     if new_balance is not None:
#                         print(f"New balance after deposit: ${new_balance:.2f}")
#                     else:
#                         print("Account not found or invalid deposit amount.")
#                 except ValueError:
#                     print("Invalid input. Account number and deposit amount must be numbers.")

#             elif command == "3":
#                 try:
#                     account_number = int(input("Enter Account Number: "))
#                     amount = float(input("Enter Withdrawal Amount: "))
#                     new_balance = self.bank.withdraw(account_number, amount)
#                     if new_balance is not None:
#                         print(f"New balance after withdrawal: ${new_balance:.2f}")
#                     else:
#                         print("Account not found or insufficient balance.")
#                 except ValueError:
#                     print("Invalid input. Account number and withdrawal amount must be numbers.")

#             elif command == "4":
#                 try:
#                     account_number = int(input("Enter Account Number: "))
#                     balance = self.bank.get_account_balance(account_number)
#                     if balance is not None:
#                         print(f"Account Balance: ${balance:.2f}")
#                     else:
#                         print("Account not found.")
#                 except ValueError:
#                     print("Invalid account number. Please enter a valid number.")

#             elif command == "5":
#                 try:
#                     from_account_number = int(input("Enter From Account Number: "))
#                     to_account_number = int(input("Enter To Account Number: "))
#                     amount = float(input("Enter Transfer Amount: "))
#                     result = self.bank.transfer(from_account_number, to_account_number, amount)
#                     if result is not None:
#                         print(f"Transfer successful. Remaining balance in From Account: ${result:.2f}")
#                     else:
#                         print("Transfer failed. Check account numbers or insufficient balance.")
#                 except ValueError:
#                     print("Invalid input. Account numbers and transfer amount must be numbers.")

#             elif command == "6":
#                 try:
#                     account_number = int(input("Enter Account Number: "))
#                     self.bank.get_account_details(account_number)
#                 except ValueError:
#                     print("Invalid account number. Please enter a valid number.")

#             elif command == "7":
#                 print("Exiting the banking system.")
#                 break

#             else:
#                 print("Invalid command. Please try again.")


# app = BankApp()
# app.main()





# ====================================================================================================================


# Task 11: Interface/abstract class, and Single Inheritance, static variable
# 1. Create a ‘Customer’ class as mentioned above task.

import re
from abc import ABC, abstractmethod  

# task 12 *******************************************
class InsufficientFundException(Exception):
    pass
class InvalidAccountException(Exception):
    pass
class OverDraftLimitExceededException(Exception):
    pass
#****************************************************

class Customer:
    def __init__(self, customer_id=None, first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.validate_email(email)
        self.phone = self.validate_phone(phone)
        self.address = address

        if self.email is None:
            raise ValueError("Invalid email format.")
        if self.phone is None:
            raise ValueError("Invalid phone number format.")

    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return email
        return None  

    def validate_phone(self, phone):
        pattern = r"^\d{10}$"
        if re.match(pattern, phone):
            return phone
        return None

    def print_info(self):
        print(f"Customer ID: {self.customer_id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\n"
              f"Email: {self.email}\nPhone: {self.phone}\nAddress: {self.address}\n")

# 2. Create an class ‘Account’ that includes the following attributes. Generate account number using 
# static variable.
# • Account Number (a unique identifier).
# • Account Type (e.g., Savings, Current)
# • Account Balance
# • Customer (the customer who owns the account)
# • lastAccNo

class Account:
    lastAccNo = 0  

    def __init__(self, account_type, customer, balance=0):
        Account.lastAccNo += 1
        self.account_number = Account.lastAccNo
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def get_balance(self):
        return self.balance

# 3. Create three child classes that inherit the Account class and each class must contain below 
# mentioned attribute:
# • SavingsAccount: A savings account that includes an additional attribute for interest rate. 
# Saving account should be created with minimum balance 500.
# • CurrentAccount: A Current account that includes an additional attribute for 
# overdraftLimit(credit limit). withdraw() method to allow overdraft up to a certain limit.
# withdraw limit can exceed the available balance and should not exceed the overdraft 
# limit.
# • ZeroBalanceAccount: ZeroBalanceAccount can be created with Zero balance.


class SavingsAccount(Account):
    def __init__(self, customer, interest_rate, balance=500):
        if balance < 500:
            raise ValueError("Minimum balance for Savings Account is 500.")
        super().__init__("Savings", customer, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.balance - amount < 500:
            raise InsufficientFundException("Withdrawal would violate minimum balance requirement.")
        self.balance -= amount
        return self.balance


class CurrentAccount(Account):
    def __init__(self, customer, overdraft_limit, balance=0):
        super().__init__("Current", customer, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit < amount:
            raise OverDraftLimitExceededException("Withdrawal exceeds overdraft limit.")
        self.balance -= amount
        return self.balance


class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("ZeroBalance", customer, 0)


# 4. Create ICustomerServiceProvider interface/abstract class with following functions:
# • get_account_balance(account_number: long): Retrieve the balance of an account given
# its account number. should return the current balance of account.
# • deposit(account_number: long, amount: float): Deposit the specified amount into the 
# account. Should return the current balance of account.
# • withdraw(account_number: long, amount: float): Withdraw the specified amount from 
# the account. Should return the current balance of account. A savings account should 
# maintain a minimum balance and checking if the withdrawal violates the minimum 
# balance rule.
# • transfer(from_account_number: long, to_account_number: int, amount: float): 
# Transfer money from one account to another.
# • getAccountDetails(account_number: long): Should return the account and customer 
# details.


class ICustomerServiceProvider(ABC):  
    @abstractmethod
    def get_account_balance(self, account_number):
        pass

    @abstractmethod
    def deposit(self, account_number, amount):
        pass

    @abstractmethod
    def withdraw(self, account_number, amount):
        pass

    @abstractmethod
    def transfer(self, from_account_number, to_account_number, amount):
        pass

    @abstractmethod
    def get_account_details(self, account_number):
        pass


# 5. Create IBankServiceProvider interface/abstract class with following functions:
# • create_account(Customer customer, long accNo, String accType, float balance): Create 
# a new bank account for the given customer with the initial balance.
# • listAccounts():Account[] accounts: List all accounts in the bank.
# • calculateInterest(): the calculate_interest() method to calculate interest based on the 
# balance and interest rate.


class IBankServiceProvider(ABC):  
    @abstractmethod
    def create_account(self, customer, acc_type, balance):
        pass

    @abstractmethod
    def list_accounts(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass



# 6. Create CustomerServiceProviderImpl class which implements ICustomerServiceProvider 
# provide all implementation methods.




class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number):
        if account_number not in self.accounts:
            raise InvalidAccountException("Account number not found.")
        return self.accounts[account_number].get_balance()

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise InvalidAccountException("Account number not found.")
        self.accounts[account_number].balance += amount
        return self.accounts[account_number].get_balance()

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise InvalidAccountException("Account number not found.")
        new_balance = self.accounts[account_number].withdraw(amount)
        return new_balance

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number not in self.accounts or to_account_number not in self.accounts:
            raise InvalidAccountException("One or both account numbers are invalid.")
        self.accounts[from_account_number].withdraw(amount)
        self.accounts[to_account_number].deposit(amount)

    def get_account_details(self, account_number):
        if account_number not in self.accounts:
            raise InvalidAccountException("Account number not found.")
        return self.accounts[account_number]

# 7. Create BankServiceProviderImpl class which inherits from CustomerServiceProviderImpl and 
# implements IBankServiceProvider
# • Attributes
# o accountList: Array of Accounts to store any account objects.
# o branchName and branchAddress as String objects



class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self):
        super().__init__()
        self.branch_name = "Main Branch"
        self.branch_address = "123 Bank St."

    def create_account(self, customer, acc_type, balance):
        if acc_type == "Savings":
            account = SavingsAccount(customer, interest_rate=0.03, balance=balance)
        elif acc_type == "Current":
            account = CurrentAccount(customer, overdraft_limit=1000, balance=balance)
        elif acc_type == "ZeroBalance":
            account = ZeroBalanceAccount(customer)
        else:
            raise ValueError("Invalid account type.")
        
        self.accounts[account.account_number] = account
        return account.account_number

    def list_accounts(self):
        return list(self.accounts.values())

    def calculate_interest(self, account_number):
        account = self.accounts.get(account_number)
        if isinstance(account, SavingsAccount):
            return account.balance * account.interest_rate
        return 0

# 8. Create BankApp class and perform following operation:
# • main method to simulate the banking system. Allow the user to interact with the system 
# by entering choice from menu such as "create_account", "deposit", "withdraw",
# "get_balance", "transfer", "getAccountDetails", "ListAccounts" and "exit."
# • create_account should display sub menu to choose type of accounts and repeat this 
# operation until user exit.
# 9. Place the interface/abstract class in service package and interface/abstract class implementation 
# class, account class in bean package and Bank class in app package.
# 10. Should display appropriate message when the account number is not found and insufficient fund
# or any other wrong information provided.

class BankApp:
    def __init__(self):
        self.bank = BankServiceProviderImpl()

    def display_menu(self):
        print("\n--- Banking System Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Get Balance")
        print("5. Transfer")
        print("6. Get Account Details")
        print("7. List Accounts")
        print("8. Exit")
        print("---------------------------")

    def main(self):
        while True:
            self.display_menu()
            command = input("Enter the number of the command you want to execute: ").strip()
            try:
                if command == "1":
                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    email = input("Enter Email: ")
                    phone = input("Enter Phone Number: ")
                    address = input("Enter Address: ")

                    customer = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address)

                    account_type = input("Choose Account Type (Savings, Current, ZeroBalance): ").strip()
                    initial_balance = float(input("Enter Initial Balance: "))

                    account_number = self.bank.create_account(customer, account_type, initial_balance)
                    print(f"Account created successfully. Account Number: {account_number}")

                elif command == "2":
                    account_number = int(input("Enter Account Number: "))
                    amount = float(input("Enter Deposit Amount: "))
                    new_balance = self.bank.deposit(account_number, amount)
                    print(f"New balance after deposit: ${new_balance:.2f}")

                elif command == "3":
                    account_number = int(input("Enter Account Number: "))
                    amount = float(input("Enter Withdrawal Amount: "))
                    new_balance = self.bank.withdraw(account_number, amount)
                    print(f"New balance after withdrawal: ${new_balance:.2f}")

                elif command == "4":
                    account_number = int(input("Enter Account Number: "))
                    balance = self.bank.get_account_balance(account_number)
                    print(f"Account Balance: ${balance:.2f}")

                elif command == "5":
                    from_account_number = int(input("Enter From Account Number: "))
                    to_account_number = int(input("Enter To Account Number: "))
                    amount = float(input("Enter Transfer Amount: "))
                    self.bank.transfer(from_account_number, to_account_number, amount)
                    print("Transfer successful.")

                elif command == "6":
                    account_number = int(input("Enter Account Number: "))
                    account_details = self.bank.get_account_details(account_number)
                    account_details.customer.print_info()
                    print(f"Account Number: {account_details.account_number}\nAccount Type: {account_details.account_type}\n"
                          f"Account Balance: ${account_details.get_balance():.2f}")

                elif command == "7":
                    accounts = self.bank.list_accounts()
                    for acc in accounts:
                        acc.customer.print_info()
                        print(f"Account Number: {acc.account_number}, Account Type: {acc.account_type}, Balance: ${acc.get_balance():.2f}")
                
                elif command == "8":
                    print("Exiting the banking system.")
                    break

                else:
                    print("Invalid command. Please try again.")

            # task12**************************************************************************************************
            except (InsufficientFundException, InvalidAccountException, OverDraftLimitExceededException) as e:
                print(f"Error: {e}")
            except ValueError as ve:
                print(f"Value Error: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            #*********************************************************************************************************
            


app = BankApp()
try:
    app.main()
except TypeError as e: 
    print(f"Null Reference Error: {e}")


# =======================================================================================================

# Task 13: Collection
# 1. From the previous task change the HMBank attribute Accounts to List of Accounts and perform 
# the same operation.
# 2. From the previous task change the HMBank attribute Accounts to Set of Accounts and perform 
# the same operation.
# • Avoid adding duplicate Account object to the set.
# • Create Comparator<Account> object to sort the accounts based on customer name 
# when listAccounts() method called.
# 3. From the previous task change the HMBank attribute Accounts to HashMap of Accounts and 
# perform the same operation




# # Using List of Accounts
# class BankServiceProviderImplList(ICustomerServiceProvider, IBankServiceProvider):
#     def __init__(self):
#         super().__init__()
#         self.accounts: List[Account] = []  # List to store accounts

#     def get_account_balance(self, account_number):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account.get_balance()
#         raise InvalidAccountException("Account number not found.")

#     def deposit(self, account_number, amount):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 account.balance += amount
#                 return account.get_balance()
#         raise InvalidAccountException("Account number not found.")

#     def withdraw(self, account_number, amount):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 new_balance = account.withdraw(amount)
#                 return new_balance
#         raise InvalidAccountException("Account number not found.")

#     def transfer(self, from_account_number, to_account_number, amount):
#         from_account = next((acc for acc in self.accounts if acc.account_number == from_account_number), None)
#         to_account = next((acc for acc in self.accounts if acc.account_number == to_account_number), None)

#         if from_account is None:
#             raise InvalidAccountException("Invalid From Account number.")
#         if to_account is None:
#             raise InvalidAccountException("Invalid To Account number.")
        
#         from_account.withdraw(amount)
#         to_account.balance += amount

#     def get_account_details(self, account_number):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account
#         raise InvalidAccountException("Account number not found.")

#     def create_account(self, customer, acc_type, balance):
#         if acc_type == "Savings":
#             account = SavingsAccount(customer, interest_rate=0.03, balance=balance)
#         elif acc_type == "Current":
#             account = CurrentAccount(customer, overdraft_limit=1000, balance=balance)
#         elif acc_type == "ZeroBalance":
#             account = ZeroBalanceAccount(customer)
#         else:
#             raise ValueError("Invalid account type.")
        
#         self.accounts.append(account)
#         return account.account_number

#     def list_accounts(self):
#         return self.accounts


# # Using Set of Accounts
# class BankServiceProviderImplSet(ICustomerServiceProvider, IBankServiceProvider):
#     def __init__(self):
#         super().__init__()
#         self.accounts: Set[Account] = set()  # Set to store unique accounts

#     def get_account_balance(self, account_number):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account.get_balance()
#         raise InvalidAccountException("Account number not found.")

#     def deposit(self, account_number, amount):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 account.balance += amount
#                 return account.get_balance()
#         raise InvalidAccountException("Account number not found.")

#     def withdraw(self, account_number, amount):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 new_balance = account.withdraw(amount)
#                 return new_balance
#         raise InvalidAccountException("Account number not found.")

#     def transfer(self, from_account_number, to_account_number, amount):
#         from_account = next((acc for acc in self.accounts if acc.account_number == from_account_number), None)
#         to_account = next((acc for acc in self.accounts if acc.account_number == to_account_number), None)

#         if from_account is None:
#             raise InvalidAccountException("Invalid From Account number.")
#         if to_account is None:
#             raise InvalidAccountException("Invalid To Account number.")
        
#         from_account.withdraw(amount)
#         to_account.balance += amount

#     def get_account_details(self, account_number):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account
#         raise InvalidAccountException("Account number not found.")

#     def create_account(self, customer, acc_type, balance):
#         if acc_type == "Savings":
#             account = SavingsAccount(customer, interest_rate=0.03, balance=balance)
#         elif acc_type == "Current":
#             account = CurrentAccount(customer, overdraft_limit=1000, balance=balance)
#         elif acc_type == "ZeroBalance":
#             account = ZeroBalanceAccount(customer)
#         else:
#             raise ValueError("Invalid account type.")
        
#         self.accounts.add(account)  # Avoid duplicates
#         return account.account_number

#     def list_accounts(self):
#         # Sort accounts based on customer name
#         sorted_accounts = sorted(self.accounts, key=lambda acc: acc.customer.first_name + ' ' + acc.customer.last_name)
#         return sorted_accounts


# # Using HashMap of Accounts
# class BankServiceProviderImplMap(ICustomerServiceProvider, IBankServiceProvider):
#     def __init__(self):
#         super().__init__()
#         self.accounts: Dict[int, Account] = {}  # HashMap to store accounts

#     def get_account_balance(self, account_number):
#         if account_number not in self.accounts:
#             raise InvalidAccountException("Account number not found.")
#         return self.accounts[account_number].get_balance()

#     def deposit(self, account_number, amount):
#         if account_number not in self.accounts:
#             raise InvalidAccountException("Account number not found.")
#         self.accounts[account_number].balance += amount
#         return self.accounts[account_number].get_balance()

#     def withdraw(self, account_number, amount):
#         if account_number not in self.accounts:
#             raise InvalidAccountException("Account number not found.")
#         new_balance = self.accounts[account_number].withdraw(amount)
#         return new_balance

#     def transfer(self, from_account_number, to_account_number, amount):
#         if from_account_number not in self.accounts:
#             raise InvalidAccountException("Invalid From Account number.")
#         if to_account_number not in self.accounts:
#             raise InvalidAccountException("Invalid To Account number.")

#         from_account = self.accounts[from_account_number]
#         to_account = self.accounts[to_account_number]

#         from_account.withdraw(amount)
#         to_account.balance += amount

#     def get_account_details(self, account_number):
#         if account_number not in self.accounts:
#             raise InvalidAccountException("Account number not found.")
#         return self.accounts[account_number]

#     def create_account(self, customer, acc_type, balance):
#         if acc_type == "Savings":
#             account = SavingsAccount(customer, interest_rate=0.03, balance=balance)
#         elif acc_type == "Current":
#             account = CurrentAccount(customer, overdraft_limit=1000, balance=balance)
#         elif acc_type == "ZeroBalance":
#             account = ZeroBalanceAccount(customer)
#         else:
#             raise ValueError("Invalid account type.")
        
#         self.accounts[account.account_number] = account
#         return account.account_number

#     def list_accounts(self):
#         return self.accounts.values()

