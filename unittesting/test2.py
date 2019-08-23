import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 20), 30)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(20, 20), 400)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(-1, 1), -1)

    def test_subtract(self):
        self.assertEqual(calc.subtract(20, 10), 10)
        self.assertEqual(calc.subtract(10, 20), -10)
        self.assertEqual(calc.subtract(1, -1), 2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_division(self):
        self.assertEqual(calc.division(20, 20), 1)
        self.assertEqual(calc.division(-1, -1), 1)
        self.assertEqual(calc.division(-1, 1), -1)
        self.assertEqual(calc.division(5, 2), 2.5)
        # self.assertRaises(ValueError, calc.division, 10, 0)
        with self.assertRaises(ZeroDivisionError):
            calc.division(20, 0)

    def test_modulo(self):
        self.assertEqual(calc.modulo(10, 5), 0)
        self.assertEqual(calc.modulo(2, 5), 2)
        with self.assertRaises(ZeroDivisionError):
            calc.modulo(5, 0)


if __name__ == "__main__":
    unittest.main()

# here v run the test for each method in calc.py
