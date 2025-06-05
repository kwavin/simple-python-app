# test_calculator.py - Unit tests for the calculator

import unittest
from main import Calculator, greet_user


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition functionality."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction functionality."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(10, 10), 0)
    
    def test_multiply(self):
        """Test multiplication functionality."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division functionality."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.333333, places=5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power functionality."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(10, 2), 100)
    
    def test_greet_user(self):
        """Test the greeting function."""
        greeting = greet_user()
        self.assertIsInstance(greeting, str)
        self.assertIn("Calculator", greeting)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_large_numbers(self):
        """Test with large numbers."""
        result = self.calc.add(999999, 1)
        self.assertEqual(result, 1000000)
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(self.calc.multiply(-5, -4), 20)
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_floating_point(self):
        """Test with floating point numbers."""
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0, places=7)


if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)
