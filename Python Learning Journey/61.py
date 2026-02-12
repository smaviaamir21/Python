class BankAccount:
    def __init__(self, balance):
        self._balance = balance   # Protected variable

    def show_balance(self):
        print("Balance:", self._balance)


acc1 = BankAccount(5000)

# Accessing (Technically possible but not recommended)
print(acc1._balance)

acc1.show_balance()
