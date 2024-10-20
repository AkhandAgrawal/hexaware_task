from entity.account import Account

class SavingsAccount(Account):
    """Class representing a savings account."""

    MIN_BALANCE = 500

    def __init__(self, customer, balance, interest_rate):
        super().__init__(customer, "Savings", balance)
        self.interest_rate = interest_rate
        if self.balance < SavingsAccount.MIN_BALANCE:
            raise ValueError("Savings account requires a minimum balance of 500.")

    def __str__(self):
        return f"SavingsAccount[{super().__str__()}, InterestRate={self.interest_rate}]"
