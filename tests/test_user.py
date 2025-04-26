import unittest
from account.user import User
from account.bank_account import BankAccount, SavingsAccount

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        """Test user initialization and properties"""
        user = User("John Doe", "john@example.com")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")  # Should match exactly what was passed in
        self.assertEqual(len(user.accounts), 0)
    
    def test_add_account(self):
        """Test adding accounts to a user"""
        user = User("Jane Doe", "jane@example.com")
        account1 = BankAccount("Jane", "jane@example.com", 500)
        account2 = SavingsAccount("Jane", "jane@example.com", 1000)
        
        user.add_account(account1)
        self.assertEqual(len(user.accounts), 1)
        
        user.add_account(account2)
        self.assertEqual(len(user.accounts), 2)
    
    def test_get_total_balance(self):
        """Test get_total_balance method"""
        user = User("Alice", "alice@example.com")
        account1 = BankAccount("Alice", "alice@example.com", 500)
        account2 = BankAccount("Alice", "alice@example.com", 1000)
        
        user.add_account(account1)
        user.add_account(account2)
        
        self.assertEqual(user.get_total_balance(), 1500)
    
    def test_remove_account(self):
        """Test removing accounts from a user"""
        user = User("Bob", "bob@example.com")
        account = BankAccount("Bob", "bob@example.com", 500)
        
        user.add_account(account)
        self.assertEqual(len(user.accounts), 1)
        
        result = user.remove_account(account)
        self.assertEqual(result, "Account removed successfully")
        self.assertEqual(len(user.accounts), 0)
        
        result = user.remove_account(account)
        self.assertEqual(result, "Account not found")
    
    def test_is_valid_email(self):
        """Test email validation method"""
        user = User("Test", "test@example.com")
        # Use a more obviously valid email address for tests
        self.assertTrue(user.is_valid_email("valid.email@example.com"))  
        self.assertFalse(user.is_valid_email("invalid-email"))  # Invalid email should fail