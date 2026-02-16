from datetime import datetime


class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp} | {self.transaction_type} | ${self.amount}"
    
class Account:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit mujst positive")
        
        self.__balance += amount
        self.transactions.append(Transaction("DEPOST", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        
        if amount > self.__balance:
            raise ValueError("Insufficient Funds")
        
        self.__balance -= amount
        self.transactions.append(Transaction("WITHDRAW", amount))

    def get_balance(self):
        return self.__balance
    
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

class Bank:
    def __init__(self):
        self.users = {}
        self.accounts = {}

    def create_user(self, user_id, name):
        if user_id in self.users:
            raise ValueError("User already exist")
        
        self.users[user_id] = User(user_id, name)
    
    def create_account(self, user_id, account_number, initial_balance=0):
        if account_number in self.accounts:
            raise ValueError("Account already exists")
        
        user = self.users.get(user_id)

        if not user:
            raise ValueError("User not Found")
        
        account = Account(account_number, initial_balance)
        user.add_account(account)
        self.accounts[account_number] = account

    def transfer(self, from_acc, to_acc, amount):
        sender = self.accounts.get(from_acc)
        receiver = self.accounts.get(to_acc)

        if not sender or not receiver:
            raise ValueError("Invalid account")
        sender.withdraw(amount)
        receiver.deposit(amount)


bank = Bank()

transaction = Transaction("WITHDRAW", 20000)

print(transaction)

bank.create_user(1, "Alice")
bank.create_user(2, "Bob")

bank.create_account(1, "A100", 500)
bank.create_account(2, "B200", 300)

bank.transfer("A100", "B200", 100)

print(bank.accounts["A100"].get_balance())
print(bank.accounts["B200"].get_balance())

        


    