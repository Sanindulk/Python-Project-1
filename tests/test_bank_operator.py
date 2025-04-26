import unittest
from unittest.mock import patch, MagicMock
from bank_operator.bank_operator import (
    validate_user_selection,
    validate_account_selection,
    validate_account_type,
    create_user,
    list_users,
    users
)
from account.user import User

class TestBankOperator(unittest.TestCase):
    def setUp(self):
        # Clear users list before each test
        users.clear()
    
    def test_validate_user_selection(self):
        """Test validate_user_selection function with valid and invalid inputs"""
        # Add a test user to the users list
        users.append(User("Test", "test@example.com"))
        
        # Valid selection
        valid, idx = validate_user_selection("1")
        self.assertTrue(valid)
        self.assertEqual(idx, 0)
        
        # Invalid selection - out of range
        valid, idx = validate_user_selection("2")
        self.assertFalse(valid)
        self.assertEqual(idx, -1)
        
        # Invalid selection - not a number
        valid, idx = validate_user_selection("abc")
        self.assertFalse(valid)
        self.assertEqual(idx, -1)
    
    def test_validate_account_type(self):
        """Test validate_account_type function"""
        # Valid account types
        valid, account_type = validate_account_type(1)  # Savings
        self.assertTrue(valid)
        self.assertEqual(account_type, "SAVINGS")
        
        valid, account_type = validate_account_type(2)  # Student
        self.assertTrue(valid)
        self.assertEqual(account_type, "STUDENT")
        
        valid, account_type = validate_account_type(3)  # Current
        self.assertTrue(valid)
        self.assertEqual(account_type, "CURRENT")
        
        # Invalid account type
        valid, account_type = validate_account_type(4)
        self.assertFalse(valid)
        self.assertIsNone(account_type)
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_create_user(self, mock_print, mock_input):
        """Test create_user function"""
        # Setup mock input to return valid test values
        mock_input.side_effect = ["John Doe", "john.doe@example.com"]
        create_user()
        
        # Check that a user was added to the list
        self.assertEqual(len(users), 1)
        # Check that the user has the name provided
        self.assertEqual(users[0].name, "John Doe")
        # Check that the email matches what was provided
        self.assertEqual(users[0].email, "john.doe@example.com")