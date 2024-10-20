from abc import ABC, abstractmethod

class IBankRepository(ABC):
    
    @abstractmethod
    def create_account(self, customer, acc_no: int, acc_type: str, balance: float):
        """Create a new bank account and store it in the database."""
        pass

    @abstractmethod
    def list_accounts(self):
        """List all accounts in the bank from the database."""
        pass

    @abstractmethod
    def get_account_balance(self, account_number: int) -> float:
        """Retrieve the balance of an account from the database."""
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float) -> float:
        """Deposit an amount into the account and update the database."""
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float) -> float:
        """Withdraw an amount from the account and update the database."""
        pass

    @abstractmethod
    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        """Transfer money from one account to another in the database."""
        pass

    @abstractmethod
    def get_account_details(self, account_number: int):
        """Return account and customer details from the database."""
        pass

    @abstractmethod
    def get_transactions(self, account_number: int, from_date: str, to_date: str):
        """Return the list of transactions from the database."""
        pass
