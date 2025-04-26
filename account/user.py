from email_validator import validate_email, EmailNotValidError

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self): 
        return sum(account.get_balance() for account in self.accounts)

    def get_account_count(self):
        return len(self.accounts)

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return f"Account removed successfully"
        return "Account not found"

    def is_valid_email(self, email):
        # Advanced email validation using email-validator library
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False


    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: Rs.{self.get_total_balance()}"
