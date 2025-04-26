import unittest
import sys
from tests.test_transaction import *
from tests.test_bank_account import *
from tests.test_user import *
from tests.test_bank_operator import *

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    
    # Run the tests
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    # Print summary
    print(f"\nTest Summary:")
    print(f"Ran {result.testsRun} tests")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    # Print failures and errors if any
    if result.failures:
        print("\nFailures:")
        for test, error in result.failures:
            print(f"{test}: {error}")
    
    if result.errors:
        print("\nErrors:")
        for test, error in result.errors:
            print(f"{test}: {error}")
    
    # Return non-zero exit code if there were failures or errors
    sys.exit(len(result.failures) + len(result.errors))