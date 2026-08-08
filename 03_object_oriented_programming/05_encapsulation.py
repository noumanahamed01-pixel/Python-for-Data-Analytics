# Encapsulation = wrapping data (attributes) and methods together.

# Private attributes → use __attribute to hide data from direct access.

# Public methods → controlled access to private data.

# Ensures data security and integrity.

# Encapsulation Example

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # private attribute (double underscore)

    # Public method to view balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

# Object
account = BankAccount("M", 5000)

# Access through methods
print("Balance:", account.get_balance())
account.deposit(1000)
account.withdraw(2000)

# Trying direct access (not recommended)
# print(account.__balance)  # This will cause an error
