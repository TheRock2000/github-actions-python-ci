import unittest
from src.calculator import add, subtract, divide 

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(6, 3), 3)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(5, 2.5), 2.5)

    def test_divide(self):
        self.assertEqual(divide(81, 9), 9)
        self.assertEqual(divide(-100, 1), -100)
        self.assertEqual(divide(5, 2.5), 2.0)
        #yaya

if __name__ == '__main__':
    unittest.main()