class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}")
        else:
            print("Invalid deposit amount")
        print(f"Current balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient funds or invalid amount")
        print(f"Current balance: ₹{self.balance}")

    def display(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: ₹", self.balance)


print("Welcome to the Bank Management System")

name = input("Enter your name: ")
account_no = input("Enter your account number: ")
balance = float(input("Enter your initial balance: ₹"))

account = BankAccount(name, account_no, balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Details")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: ₹"))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: ₹"))
        account.withdraw(amount)

    elif choice == '3':
        account.display()

    elif choice == '4':
        print("Thank you for using the Bank Management System.")
        break

    else:
        print("Invalid choice! Try again.")
