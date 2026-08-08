#This is where you define your own error types to make programs more meaningful and user‑friendly.

# Defining a custom exception
class InsufficientBalanceError(Exception):
    def __init__(self, message="Balance is too low for withdrawal"):
        self.message = message
        super().__init__(self.message)

# Using the custom exception
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            # Raise custom exception
            raise InsufficientBalanceError(
                f"Attempted to withdraw ₹{amount}, but balance is only ₹{self.balance}"
            )
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Current Balance: ₹{self.balance}")

# Demo
account = BankAccount("M", 5000)

try:
    account.withdraw(6000)   # This will trigger custom exception
except InsufficientBalanceError as e:
    print("Error:", e)
