# test_vaultsafe.py
"""
Tests for VaultSafe module.
"""

import unittest
from vaultsafe import VaultSafe

class TestVaultSafe(unittest.TestCase):
    """Test cases for VaultSafe class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VaultSafe()
        self.assertIsInstance(instance, VaultSafe)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VaultSafe()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
