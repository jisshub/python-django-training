import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 20)
        self.assertEqual(result, 30)

    def test_multiply(self):
        result = calc.multiply(10, 20)
        self.assertNotEqual(result, 300)


if __name__ == '__main__':
    unittest.main()

# this condition will always b executed as true and the following code will execute all
# the test in the file.

# in case a test fails an assertion error is raised.
