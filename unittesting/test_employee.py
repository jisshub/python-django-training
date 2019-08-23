import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):
    def test_emp(self):
        emp1 = Employee('jiss', 'jose', 400)

        emp1.apply_raise

        self.assertEqual(emp1.pay, 800)


if __name__ == '__main__':
    unittest.main()

# here  v text whther value of apply_raise and pay are equal.
