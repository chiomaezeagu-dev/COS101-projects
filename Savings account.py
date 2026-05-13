from Account import Account

class Savings(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02
        self.withdraw_limit = 100

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal failed: Amount exceeds the ${self.withdraw_limit} limit.")
        else:
            super().withdraw(amount)

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} applied. New balance: {self.get_balance()}")


# --- Test the savings account ---
print("---Savings Account---")
savings = Savings("Alice", 1000)
print(f"Initial balance: {savings.get_balance()}")

# This will work because it is under 100
savings.withdraw(50)

# This will trigger the new limit check
# (This should now print the failure message)
savings.withdraw(150)

savings.apply_interest()

