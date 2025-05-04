class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable (Encapsulation)

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance  # Accessing private data using a method

# Creating an account
account = BankAccount("Akash", 1000)
account.deposit(500)  # Depositing money
account.withdraw(200)  # Withdrawing money
print(account.get_balance())  # Checking balance

# Trying to access the balance directly
print(account.__balance)  # This will show an error because balance is private!
