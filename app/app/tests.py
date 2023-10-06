"""
Sample Tests
"""

from django.test import SimpleTestCase
from app import calc

class calcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test that two numbers are added together."""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test that two numbers are added together."""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)