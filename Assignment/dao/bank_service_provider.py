from abc import ABC, abstractmethod

class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, acc_no: int, acc_type: str, balance: float):
        """Create a new bank account for the given customer with the initial balance."""
        pass

    @abstractmethod
    def list_accounts(self):
        """List all accounts in the bank."""
        pass

    @abstractmethod
    def get_account_details(self, account_number: int):
        """Return the account and customer details."""
        pass

    @abstractmethod
    def calculate_interest(self):
        """Calculate interest based on the balance and interest rate."""
        pass
