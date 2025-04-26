import unittest
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

class TestBankAccount(unittest.TestCase):
    def test_bank_account_initialization(self):
        """Test bank account initialization with default and custom values"""
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0)
        self.assertEqual(account.get_name(), "John")
        
        custom_account = BankAccount("Alice", "alice@example.com", 1000)
        self.assertEqual(custom_account.get_balance(), 1000)
        self.assertEqual(custom_account.get_name(), "Alice")
    
    def test_deposit_withdraw(self):
        """Test deposit and withdraw functionality"""
        account = BankAccount(initial_balance=500)
        self.assertTrue(account.deposit(200))
        self.assertEqual(account.get_balance(), 700)
        
        self.assertTrue(account.withdraw(300))
        self.assertEqual(account.get_balance(), 400)
        
    def test_invalid_operations(self):
        """Test invalid deposit and withdraw operations"""
        account = BankAccount(initial_balance=500)
        self.assertFalse(account.deposit(-100))
        self.assertEqual(account.get_balance(), 500)
        
        self.assertFalse(account.withdraw(600))  # Insufficient balance
        self.assertEqual(account.get_balance(), 500)
        
class TestSavingsAccount(unittest.TestCase):
    def test_savings_account_minimum_balance(self):
        """Test savings account minimum balance requirement"""
        savings = SavingsAccount(initial_balance=200)
        self.assertEqual(savings.get_balance(), 200)
        
        # Should fail as it would leave less than minimum balance
        self.assertFalse(savings.withdraw(150))
        self.assertEqual(savings.get_balance(), 200)
        
        # Should succeed as it leaves minimum balance
        self.assertTrue(savings.withdraw(100))
        self.assertEqual(savings.get_balance(), 100)

class TestStudentAccount(unittest.TestCase):
    def test_student_account_minimum_balance(self):
        """Test student account minimum balance requirement"""
        student = StudentAccount(initial_balance=200)
        self.assertEqual(student.get_balance(), 200)
        
        # Should fail as it would leave less than minimum balance
        self.assertFalse(student.withdraw(150))
        self.assertEqual(student.get_balance(), 200)
        
        # Should succeed as it leaves minimum balance
        self.assertTrue(student.withdraw(100))
        self.assertEqual(student.get_balance(), 100)