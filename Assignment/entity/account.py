class Account:
    last_account_number = 1000

    def __init__(self, account_type: str, balance: float, customer):
        Account.last_account_number += 1
        self._account_number = Account.last_account_number
        self._account_type = account_type
        self._balance = float(balance)  # Ensure balance is a float
        self._customer = customer

    @property
    def account_number(self) -> int:
        return self._account_number

    @property
    def account_type(self) -> str:
        return self._account_type

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def customer(self):
        return self._customer

    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value

    @customer.setter
    def customer(self, value):
        self._customer = value

    def deposit(self, amount: float) -> float:
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance    

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self._balance}.")
            return self._balance
        else:
            raise ValueError("Insufficient balance for withdrawal.")

    def calculate_interest(self):
        if self._account_type.lower() == "savings":  # Make case-insensitive
            interest_rate = 0.045
            interest_amount = self._balance * interest_rate
            self.deposit(interest_amount)
            print(f"Interest of {interest_amount:.2f} added to the account.")

    def transfer(self, to_account, amount: float):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds for transfer.")
        else:
            self._balance -= amount
            to_account.deposit(amount)
            print(f"Transfer of {amount} to Account {to_account.account_number} successful.")

    def __str__(self):
        return (f"Account Number: {self._account_number}\n"
                f"Account Type: {self._account_type}\n"
                f"Balance: {self._balance}\n"
                f"Customer: {self._customer}")
