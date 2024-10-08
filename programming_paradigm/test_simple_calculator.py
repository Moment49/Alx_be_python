import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, 0), -1)
        self.assertEqual(self.calc.add(-1, -10), -11)
        # Add more assertions to thoroughly test the add method.
    
    def test_subtraction(self):
        "Test the subtraction method"
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(0, 2), -2)
        
    def test_multiplication(self):
        "Test the subtraction method"
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(-3, -2), 6)
        self.assertEqual(self.calc.multiply(0, 2), 0)
        self.assertEqual(self.calc.multiply(-10, 2), -20)

    def test_division(self):
        "Test the subtraction method"
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(10, 0), None)
        self.assertEqual(self.calc.divide(0, 2), 0)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(-4, 2), -2)

if __name__ == "__main__":
    unittest.main()