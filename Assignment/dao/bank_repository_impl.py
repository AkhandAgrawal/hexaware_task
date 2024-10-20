import pyodbc
from dao.bank_repository import IBankRepository
from entity.account import Account
from entity.customer import Customer

class BankRepositoryImpl(IBankRepository):
    def __init__(self):
        self.conn = self.get_db_connection()

    def get_db_connection(self):
        try:
            connection_string = (
                "Driver={ODBC Driver 18 for SQL Server};"
                "Server=AKHAND\\SQLEXPRESS;"
                "Database=HMBank;"
                "TrustServerCertificate=yes;"
                "Trusted_Connection=yes;"
            )
            return pyodbc.connect(connection_string)
        except Exception as e:
            print(f"Error while connecting to the DB: {e}")
            return None

    def create_account(self, customer, acc_no: int, acc_type: str, balance: float):
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO Accounts (account_id, customer_id, account_type, balance)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (acc_no, customer.customer_id, acc_type, balance))
            self.conn.commit()
            print(f"Account created successfully for customer ID {customer.customer_id}")
        except Exception as e:
            print(f"Error creating account in DB: {e}")

    def list_accounts(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM Accounts"
            cursor.execute(query)
            accounts = cursor.fetchall()
            for account in accounts:
                print(f"Account ID: {account[0]}, Customer ID: {account[1]}, Type: {account[2]}, Balance: {account[3]}")
            return accounts
        except Exception as e:
            print(f"Error listing accounts from DB: {e}")

    def get_account_balance(self, account_number: int) -> float:
        try:
            cursor = self.conn.cursor()
            query = "SELECT balance FROM Accounts WHERE account_id = ?"
            cursor.execute(query, (account_number,))
            balance = cursor.fetchone()
            if balance:
                return balance[0]
            else:
                print(f"Account {account_number} not found.")
                return 0.0
        except Exception as e:
            print(f"Error getting account balance from DB: {e}")
            return 0.0

    def deposit(self, account_number: int, amount: float) -> float:
        try:
            cursor = self.conn.cursor()
            current_balance = self.get_account_balance(account_number)
            new_balance = current_balance + amount
            query = "UPDATE Accounts SET balance = ? WHERE account_id = ?"
            cursor.execute(query, (new_balance, account_number))
            self.conn.commit()
            print(f"Deposited {amount} into account {account_number}. New balance: {new_balance}")
            return new_balance
        except Exception as e:
            print(f"Error depositing to account in DB: {e}")
            return 0.0

    def withdraw(self, account_number: int, amount: float) -> float:
        try:
            cursor = self.conn.cursor()
            current_balance = self.get_account_balance(account_number)
            if current_balance >= amount:
                new_balance = current_balance - amount
                query = "UPDATE Accounts SET balance = ? WHERE account_id = ?"
                cursor.execute(query, (new_balance, account_number))
                self.conn.commit()
                print(f"Withdrawn {amount} from account {account_number}. New balance: {new_balance}")
                return new_balance
            else:
                print("Insufficient balance for withdrawal.")
                return current_balance
        except Exception as e:
            print(f"Error withdrawing from account in DB: {e}")
            return 0.0

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        try:
            # Check balance in from_account
            from_balance = self.get_account_balance(from_account_number)
            if from_balance >= amount:
                # Withdraw from from_account
                self.withdraw(from_account_number, amount)
                # Deposit into to_account
                self.deposit(to_account_number, amount)
                print(f"Transferred {amount} from account {from_account_number} to account {to_account_number}.")
            else:
                print("Insufficient funds for transfer.")
        except Exception as e:
            print(f"Error transferring funds in DB: {e}")

    def get_account_details(self, account_number: int):
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT Accounts.account_id, Accounts.account_type, Accounts.balance, 
                    Customers.customer_id, Customers.first_name, Customers.last_name, 
                    Customers.dob, Customers.email, Customers.phone_number, Customers.address 
                FROM Accounts 
                JOIN Customers ON Accounts.customer_id = Customers.customer_id 
                WHERE Accounts.account_id = ?
            """
            cursor.execute(query, (account_number,))
            account_details = cursor.fetchone()
            if account_details:
                # Unpack the values from the query result
                account_id, account_type, balance, customer_id, first_name, last_name, dob, email, phone_number, address = account_details
                
                # Create Customer instance
                customer = Customer(customer_id, first_name, last_name, dob, email, phone_number, address)
                
                # Create Account instance with the correct parameters
                account = Account(account_type, balance, customer)  # account_type and balance are correct
                
                print(f"Account Details for {account_number}:\n{account}")  # Print account details
                return account  # Return the Account object if needed
            else:
                print(f"Account {account_number} not found.")
                return None
        except Exception as e:
            print(f"Error getting account details from DB: {e}")


    def get_transactions(self, account_number: int, from_date: str, to_date: str):
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT * FROM Transactions 
                WHERE account_id = ? AND transaction_date BETWEEN ? AND ?
            """
            cursor.execute(query, (account_number, from_date, to_date))
            transactions = cursor.fetchall()
            for transaction in transactions:
                print(transaction)
            return transactions
        except Exception as e:
            print(f"Error getting transactions from DB: {e}")

    def get_customer_details(self, customer_id: int):
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT customer_id, first_name, last_name, dob, email, phone_number, address 
                FROM Customers 
                WHERE customer_id = ?
            """
            cursor.execute(query, (customer_id,))
            customer_data = cursor.fetchone()
            if customer_data:
                customer = Customer(*customer_data)  # Unpack the values into the Customer constructor
                return customer
            else:
                print("Customer not found.")
                return None
        except Exception as e:
            print(f"Error getting customer details from DB: {e}")
            return None
