class Transaction:
    def __init__(self, account, description, transaction_type, transaction_amount, date_time):
        self.account = account
        self.description = description
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.date_time = date_time

    def __str__(self):
        return f"Transaction[Account={self.account.account_number}, Description={self.description}, " \
               f"Type={self.transaction_type}, Amount={self.transaction_amount}, DateTime={self.date_time}]"
