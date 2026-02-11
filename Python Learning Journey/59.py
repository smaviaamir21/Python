class BankAccount:
    bank_name = "National Bank"   # Class variable

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # Instance Method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid amount!")

    # Instance Method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    # Instance Method
    def show_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

    # Class Method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print("Bank name updated successfully.")

    # Static Method
    @staticmethod
    def bank_policy():
        print("Minimum balance should be 500.")


# Creating objects
acc1 = BankAccount("Smavia", 5000)
acc2 = BankAccount("Ayesha", 3000)

# Using instance methods
acc1.deposit(1000)
acc1.withdraw(2000)
acc1.show_balance()

# Using class method
BankAccount.change_bank_name("International Bank")
print("New Bank Name:", BankAccount.bank_name)

# Using static method
BankAccount.bank_policy()
