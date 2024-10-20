from entity.account import Account

class ZeroBalanceAccount(Account):
    """Class representing a zero-balance account."""

    def __init__(self, customer):
        super().__init__(customer, "ZeroBalance", 0)

    def __str__(self):
        return f"ZeroBalanceAccount[{super().__str__()}]"
