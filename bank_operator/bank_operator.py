from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Invalid email address!")
        return
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    # Check if users list is empty
    if not users:
        print("No users available. Please create a user first")
        return
        
    list_users()
    try:
        idx = int(input("Select user number: ")) - 1
        # Validate user index
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
            
        print("Account Type:")
        print("1. Savings Account")
        print("2. Students Account")
        print("3. Current Account")
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))

        if account_choice == 1:
            account = SavingsAccount(users[idx].name, users[idx].email, amount)
        elif account_choice == 2:
            account = StudentAccount(users[idx].name, users[idx].email, amount)
        elif account_choice == 3:
            account = CurrentAccount(users[idx].name, users[idx].email, amount)
        else:
            print("Invalid account type!")
            return

        users[idx].add_account(account)
        print(f"{account.get_account_type()} added!\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def deposit_money():
    # Check if users list is empty
    if not users:
        print("No users available. Please create a user first.")
        return
        
    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        # Validate user index
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
            
        user = users[idx]
        if not user.accounts:
            print("This user has no accounts. Please create an account first.\n")
            return
            
        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
        acc_idx = int(input("Select account: ")) - 1
        
        # Validate account index
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid user selection.\n")
            return
            
        amount = float(input("Enter amount to deposit: "))
        user.accounts[acc_idx].deposit(amount)
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def withdraw_money():
    # Check if users list is empty
    if not users:
        print("No users available. Please create a user first.")
        return
        
    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        # Validate user index
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
            
        user = users[idx]
        if not user.accounts:
            print("This user has no accounts. Please create an account first.\n")
            return
            
        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
        acc_idx = int(input("Select account: ")) - 1
        
        # Validate account index
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid user selection.\n")
            return
            
        amount = float(input("Enter amount to withdraw: "))
        try:
            user.accounts[acc_idx].withdraw(amount)
            print("Withdrawal successful.\n")
        except ValueError as e:
            print(f"Error: {e}\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def view_transactions():
    # Check if users list is empty
    if not users:
        print("No users available. Please create a user first.")
        return
        
    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        # Validate user index
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
            
        user = users[idx]
        if not user.accounts:
            print("This user has no accounts. Please create an account first.\n")
            return
            
        for i, acc in enumerate(user.accounts):
            print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
            for tx in acc.get_transaction_history():
                print(tx)
    except ValueError:
        print("Invalid input. Please enter a number.\n")

