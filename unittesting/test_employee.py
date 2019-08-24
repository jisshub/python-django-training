import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):

    def test_email(self):
        emp1 = Employee('jiss', 'jose', 3000)
        emp2 = Employee('isco', 'alarcon', 5000)

        var1 = emp1.email
        var2 = emp2.email

        self.assertEqual(var1, 'jissjose@gmail.com')
        self.assertEqual(var2, 'iscoalarcon@gmail.com')

        emp1.first = 'john'
        emp2.last = 'james'

        self.assertEqual(emp1.email, 'johnjose@gmail.com')
        self.assertEqual(emp2.email, 'iscojames@gmail.com')

    def test_fullname(self):
        emp1 = Employee('jiss', 'jose', 3000)
        emp2 = Employee('isco', 'alarcon', 1000)

        self.assertEqual(emp1.full_name, 'jiss jose')
        emp1.first = 'jom'
        emp1.last = 'thomas'
        self.assertEqual(emp1.full_name, 'jom thomas')

        self.assertEqual(emp2.full_name, 'isco alarcon')
        emp2.first = 'alvaro'
        emp2.last = 'morata'
        self.assertEqual(emp2.full_name, 'alvaro morata')

    def test_pay(self):
        emp1 = Employee('jiss', 'jose', 6000)

        self.assertEqual(emp1.apply_raise, 12000)
        emp1.pay_raise = 1.5
        self.assertEqual(emp1.apply_raise, 18000)


if __name__ == '__main__':
    unittest.main()

# here  v text whether value of apply_raise and pay are equal.
# problem with the code is, for each test v create same object again and again
# NO DRY PRINCIPLE HERE
# check test_employee2.py
#