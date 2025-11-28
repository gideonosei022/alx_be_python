class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def display_balance(self):
         print(f"Current Balance: ${self.balance}")
    
    def get_account_info(self):
        return {
            "account_number": self.account_number,
            "account_holder": self.account_holder,
            "balance": self.balance
        }

account = BankAccount("001", "Gideon", 100)
account.deposit(50)
account.display_balance()