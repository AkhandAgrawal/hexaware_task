from dao.bank_repository import IBankRepository
from dao.customer_service_provider_impl import CustomerServiceProviderImpl
from entity.current_account import CurrentAccount
from entity.savings_account import SavingsAccount


class BankServiceProviderImpl(CustomerServiceProviderImpl):
    def __init__(self, account_repository: IBankRepository):
        super().__init__(account_repository)  # Pass the repository to the parent class
        self.account_list = []
        self.transaction_list = []

    def create_account(self, customer, acc_no: int, acc_type: str, balance: float):
        try:
            if acc_type == "Savings":
                account = SavingsAccount(customer, balance, interest_rate=0.05)
            elif acc_type == "Current":
                account = CurrentAccount(customer, balance, overdraft_limit=1000)
            else:
                raise ValueError("Invalid account type.")

            self.account_repository.create_account(account)
            self.account_list.append(account)
        except Exception as e:
            print(f"Error creating account: {e}")


    def list_accounts(self):
        try:
            return self.account_repository.list_accounts()
        except Exception as e:
            print(f"Error listing accounts: {e}")

    def get_account_details(self, account_number: int):
        try:
            return self.account_repository.get_account_details(account_number)
        except Exception as e:
            print(f"Error getting account details: {e}")

    def calculate_interest(self):
        try:
            # Logic to calculate interest for accounts can be added here
            pass
        except Exception as e:
            print(f"Error calculating interest: {e}")

    def deposit(self, account_number: int, amount: float) -> float:
        """Deposit money into an account."""
        return self.account_repository.deposit(account_number, amount)
    
