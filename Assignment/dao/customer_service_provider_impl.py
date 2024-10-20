from dao.customer_service_provider import ICustomerServiceProvider
from exception.insufficient_fund_exception import InsufficientFundException

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def get_account_balance(self, account_number: int) -> float:
        try:
            account = self.account_repository.get_account_details(account_number)
            return account.get_balance()
        except Exception as e:
            print(f"Error getting account balance: {e}")

    def deposit(self, account_number: int, amount: float) -> float:
        try:
            account = self.account_repository.get_account_details(account_number)
            account.deposit(amount)
            self.account_repository.update_account(account)
            return account.get_balance()
        except Exception as e:
            print(f"Error during deposit: {e}")

    def withdraw(self, account_number: int, amount: float) -> float:
        try:
            account = self.account_repository.get_account_details(account_number)
            account.withdraw(amount)
            self.account_repository.update_account(account)
            return account.get_balance()
        except InsufficientFundException as e:
            print(f"Insufficient funds: {e}")
        except Exception as e:
            print(f"Error during withdrawal: {e}")

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        try:
            from_account = self.account_repository.get_account_details(from_account_number)
            to_account = self.account_repository.get_account_details(to_account_number)
            from_account.withdraw(amount)
            to_account.deposit(amount)
            self.account_repository.update_account(from_account)
            self.account_repository.update_account(to_account)
        except InsufficientFundException as e:
            print(f"Insufficient funds for transfer: {e}")
        except Exception as e:
            print(f"Error during transfer: {e}")

    def get_account_details(self, account_number: int):
        try:
            return self.account_repository.get_account_details(account_number)
        except Exception as e:
            print(f"Error getting account details: {e}")

    def get_transactions(self, account_number: int, from_date: str, to_date: str):
        try:
            return self.account_repository.get_transactions(account_number, from_date, to_date)
        except Exception as e:
            print(f"Error getting transactions: {e}")
