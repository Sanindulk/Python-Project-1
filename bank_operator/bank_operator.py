from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def validate_user_selection(user_input):
    """
    Validates user selection input.
    Returns a tuple of (is_valid, index)
    """
    try:
        idx = int(user_input)
        if idx < 1 or idx > len(users):
            print("Invalid user selection.\n")
            return False, -1
        return True, idx - 1
    except ValueError:
        print("Invalid user selection.\n")
        return False, -1

def validate_account_selection(user, acc_input):
    """
    Validates account selection input.
    Returns a tuple of (is_valid, index)
    """
    try:
        acc_idx = int(acc_input) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid account selection.\n")
            return False, -1
        return True, acc_idx
    except ValueError:
        print("Invalid account selection.\n")
        return False, -1

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
    user_input = input("Select user number: ")
    valid, idx = validate_user_selection(user_input)
    if not valid:
        return
            
    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    
    try:
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        if account_choice not in [1, 2, 3]:
            print("Invalid account type!")
            return
            
        amount = float(input("Enter initial deposit: "))
        
        # Validate initial deposit amount
        if not isinstance(amount, (int, float)) or amount < 0:
            print("Initial deposit must be a non-negative number!")
            return
            
        # For savings account, check minimum balance
        if account_choice == 1 and amount < 100:
            print("Savings accounts require a minimum initial deposit of Rs.100!")
            return
            
        # For student account, check minimum balance
        if account_choice == 2 and amount < 100:
            print("Student accounts require a minimum initial deposit of Rs.100!")
            return

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
    user_input = input("Select user: ")
    valid, idx = validate_user_selection(user_input)
    if not valid:
        return
            
    user = users[idx]
    if not user.accounts:
        print("This user has no accounts. Please create an account first.\n")
        return
            
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    
    acc_input = input("Select account: ")
    valid, acc_idx = validate_account_selection(user, acc_input)
    if not valid:
        return
        
    try:
        amount = float(input("Enter amount to deposit: "))
        # Add numerical boundary check
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit amount must be a positive number!")
            return
        user.accounts[acc_idx].deposit(amount)
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def withdraw_money():
    # Check if users list is empty
    if not users:
        print("No users available. Please create a user first.")
        return
        
    list_users()
    user_input = input("Select user: ")
    valid, idx = validate_user_selection(user_input)
    if not valid:
        return
            
    user = users[idx]
    if not user.accounts:
        print("This user has no accounts. Please create an account first.\n")
        return
            
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    
    acc_input = input("Select account: ")
    valid, acc_idx = validate_account_selection(user, acc_input)
    if not valid:
        return
        
    try:
        amount = float(input("Enter amount to withdraw: "))
        # Add numerical boundary check
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount must be a positive number!")
            return
        
        # Check if amount exceeds balance before attempting withdrawal
        if amount > user.accounts[acc_idx].get_balance():
            print("Insufficient Balance!")
            return
            
        success = user.accounts[acc_idx].withdraw(amount)
        if success:
            print("Withdrawal successful.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def view_transactions():
    # Check if users list is empty
    if not users:
        print("No users available. Please create a user first.")
        return
        
    list_users()
    user_input = input("Select user: ")
    valid, idx = validate_user_selection(user_input)
    if not valid:
        return
            
    user = users[idx]
    if not user.accounts:
        print("This user has no accounts. Please create an account first.\n")
        return
            
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        for tx in acc.get_transaction_history():
            print(tx)

