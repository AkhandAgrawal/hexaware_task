import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from dao.bank_repository_impl import BankRepositoryImpl
from dao.bank_service_provider_impl import BankServiceProviderImpl
from entity.customer import Customer
from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount
from entity.zero_balance_account import ZeroBalanceAccount
from exception.insufficient_fund_exception import InsufficientFundException
from exception.invalid_account_exception import InvalidAccountException
from exception.overdraft_limit_exceeded_exception import OverdraftLimitExceededException


class BankApp:
    """Main application class for the banking system."""

    def __init__(self):
        self.account_repository = BankRepositoryImpl()  # Create an instance of your repository
        self.bank_service = BankServiceProviderImpl(self.account_repository)

    def display_menu(self):
        """Displays the main menu and handles user choices."""
        while True:
            print("\nWelcome to the Banking System")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Get Transactions")
            print("9. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.get_balance()
            elif choice == "5":
                self.transfer()
            elif choice == "6":
                self.get_account_details()
            elif choice == "7":
                self.list_accounts()
            elif choice == "8":
                self.get_transactions()
            elif choice == "9":
                print("Thank you for using the Banking System!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        """Allows the user to create a new account."""
        while True: 
            print("\nSelect Account Type:")
            print("1. Savings Account")
            print("2. Current Account")
            print("3. Zero Balance Account")
            print("4. Exit to Main Menu")
            account_type = input("Enter account type (1-4): ")

            if account_type == "1":
                customer = self.get_customer_details()
                initial_balance = float(input("Enter initial deposit for Savings Account: "))
                if initial_balance < 500:
                    print("Minimum balance for Savings Account is 500.")
                    continue
                self.bank_service.create_account(customer, 1, "Savings", initial_balance)
                print("Savings Account created successfully.")
            elif account_type == "2":
                customer = self.get_customer_details()
                initial_balance = float(input("Enter initial deposit for Current Account: "))
                overdraft_limit = float(input("Enter overdraft limit: "))
                self.bank_service.create_account(customer, 2, "Current", initial_balance)
                print("Current Account created successfully.")
            elif account_type == "3":
                customer = self.get_customer_details()
                self.bank_service.create_account(customer, 3, "ZeroBalance", 0)
                print("Zero Balance Account created successfully.")
            elif account_type == "4":
                print("Exiting to Main Menu.")
                break
            else:
                print("Invalid account type selected.")

    def get_customer_details(self):
        customer_id = input("Enter Customer ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")  
        email = input("Enter Email: ")
        phone_number = input("Enter Phone Number: ")  
        address = input("Enter Address: ")

        return Customer(customer_id, first_name, last_name, dob, email, phone_number, address)


    def deposit(self):
        """Allows the user to deposit money into an account."""
        account_number = int(input("Enter Account Number: "))  # Ensure it's an integer
        amount = float(input("Enter Amount to Deposit: "))
        
        # Get account using the bank service
        account = self.bank_service.get_account_details(account_number)
        
        if account:  # Check if account was retrieved
            try:
                new_balance = account.deposit(amount)  # Call deposit on the Account instance
                print(f"New Balance after deposit: {new_balance}")
            except Exception as e:
                print(f"Error during deposit: {e}")
        else:
            print("Account not found.")

    def withdraw(self):
        """Allows the user to withdraw money from an account."""
        account_number = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Withdraw: "))
        try:
            new_balance = self.bank_service.withdraw(account_number, amount)
            print(f"New Balance after withdrawal: {new_balance}")
        except Exception as e:
            print(f"Error during withdrawal: {e}")

    def get_balance(self):
        """Retrieves and displays the account balance."""
        account_number = input("Enter Account Number: ")
        try:
            balance = self.bank_service.get_account_balance(account_number)
            print(f"Current Balance: {balance}")
        except Exception as e:
            print(f"Error retrieving balance: {e}")

    def transfer(self):
        """Allows the user to transfer money between accounts."""
        from_account_number = input("Enter From Account Number: ")
        to_account_number = input("Enter To Account Number: ")
        amount = float(input("Enter Amount to Transfer: "))
        try:
            new_balance = self.bank_service.transfer(from_account_number, to_account_number, amount)
            print(f"New Balance after transfer: {new_balance}")
        except Exception as e:
            print(f"Error during transfer: {e}")

    def get_account_details(self):
        """Retrieves and displays account details."""
        account_number = input("Enter Account Number: ")
        try:
            details = self.bank_service.get_account_details(account_number)
        except Exception as e:
            print(f"Error retrieving account details: {e}")

    def list_accounts(self):
        """Lists all accounts in the bank."""
        try:
            accounts = self.bank_service.list_accounts()
            for account in accounts:
                print(account)
        except Exception as e:
            print(f"Error retrieving accounts: {e}")

    def get_transactions(self):
        """Retrieves and displays transactions for a specified account."""
        account_number = input("Enter Account Number: ")
        from_date = input("Enter From Date (YYYY-MM-DD): ")
        to_date = input("Enter To Date (YYYY-MM-DD): ")
        try:
            transactions = self.bank_service.get_transactions(account_number, from_date, to_date)
            # for transaction in transactions:
            #     print(transaction)
        except Exception as e:
            print(f"Error retrieving transactions: {e}")


app = BankApp()
app.display_menu()
