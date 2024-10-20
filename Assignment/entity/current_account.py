from entity.account import Account

class CurrentAccount(Account):
    """Class representing a current account."""

    def __init__(self, customer, balance, overdraft_limit):
        super().__init__(customer, "Current", balance)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"CurrentAccount[{super().__str__()}, OverdraftLimit={self.overdraft_limit}]"
