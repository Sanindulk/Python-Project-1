import unittest
from account.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        """Test transaction initialization and string representation"""
        tx = Transaction(100, "deposit")
        self.assertEqual(tx.amount, 100)
        self.assertEqual(tx.transaction_type, "deposit")
        self.assertIn("DEPOSIT", str(tx))
        
    def test_invalid_transaction_type(self):
        """Test that invalid transaction types raise ValueError"""
        with self.assertRaises(ValueError):
            Transaction(100, "invalid_type")