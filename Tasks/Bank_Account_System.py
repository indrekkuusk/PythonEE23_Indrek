# Bank Account System: Create a hierarchy of bank accounts (e.g., SavingsAccount, PayPalAccount, UnderThePillowAccount) where each account has common
# attributes (e.g., balance, account number) and specific attributes/methods. Implement polymorphic methods such as withdrawing or depositing money
# for each account type.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class PayPalAccount(BankAccount):
    def __init__(self, account_number, email, balance=0):
        super().__init__(account_number, balance)
        self.email = email

    def send_money(self, recipient_email, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Money sent to {recipient_email}"
        else:
            return "Insufficient funds"

class UnderThePillowAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.savings = 0

    def hide_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.savings += amount
            return f"${amount} hidden under the pillow"
        else:
            return "Insufficient funds"

# Example usage:
savings_account = SavingsAccount("SA001", 1000)
print("Savings Account Balance:", savings_account.balance)
print("Savings Account Interest:", savings_account.calculate_interest())

paypal_account = PayPalAccount("PP001", "example@example.com", 500)
print("PayPal Account Balance:", paypal_account.balance)
print(paypal_account.send_money("recipient@example.com", 100))
print("PayPal Account Balance after sending money:", paypal_account.balance)

pillow_account = UnderThePillowAccount("UP001", 200)
print("Under the Pillow Account Balance:", pillow_account.balance)
print(pillow_account.hide_money(50))
print("Under the Pillow Account Balance after hiding money:", pillow_account.balance)
print("Savings under the pillow:", pillow_account.savings)


# This code defines a base class BankAccount with common attributes like account number and balance, along with methods for depositing and withdrawing money.
# Then, three subclasses SavingsAccount, PayPalAccount, and UnderThePillowAccount are created with their own specific attributes and methods,
# like calculating interest for savings accounts, sending money for PayPal accounts, and hiding money under the pillow for the last account.