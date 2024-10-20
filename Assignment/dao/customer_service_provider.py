from abc import ABC, abstractmethod

class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, account_number: int) -> float:
        """Retrieve the balance of an account given its account number."""
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float) -> float:
        """Deposit the specified amount into the account."""
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float) -> float:
        """Withdraw the specified amount from the account."""
        pass

    @abstractmethod
    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        """Transfer money from one account to another."""
        pass

    @abstractmethod
    def get_account_details(self, account_number: int):
        """Return the account and customer details."""
        pass

    @abstractmethod
    def get_transactions(self, account_number: int, from_date: str, to_date: str):
        """Return the list of transactions between two dates."""
        pass
