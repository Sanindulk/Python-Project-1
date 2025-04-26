from datetime import datetime

class Transaction:
    VALID_TRANSACTION_TYPES = ["deposit", "withdraw"]
    
    def __init__(self, amount, transaction_type):
        self.amount = amount
        transaction_type = transaction_type.lower()
        if transaction_type not in self.VALID_TRANSACTION_TYPES:
            raise ValueError(f"Transaction type must be one of: {', '.join(self.VALID_TRANSACTION_TYPES)}")
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.upper()}: Rs.{self.amount}"
