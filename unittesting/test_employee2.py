import unittest

# here v import Employee class employee module(employee.py)
from employee import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        print('setup\n')
        # here v create two employee obj instead of creating them for each test.
        # ENSURING DRY PRINCIPLE
        self.emp1 = Employee('jiss', 'jose', 3000)
        self.emp2 = Employee('isco', 'alarcon', 5000)

    def tearDown(self):
        print('teardown\n')

    def test_email(self):
        print('test_email\n')
        var1 = self.emp1.email
        var2 = self.emp2.email

        self.assertEqual(var1, 'jissjose@gmail.com')
        self.assertEqual(var2, 'iscoalarcon@gmail.com')

        self.emp1.first = 'john'
        self.emp2.last = 'james'

        self.assertEqual(self.emp1.email, 'johnjose@gmail.com')
        self.assertEqual(self.emp2.email, 'iscojames@gmail.com')

    def test_fullname(self):
        print('test_fullname\n')
        self.assertEqual(self.emp1.full_name, 'jiss jose')
        self.emp1.first = 'jom'
        self.emp1.last = 'thomas'
        self.assertEqual(self.emp1.full_name, 'jom thomas')

        self.assertEqual(self.emp2.full_name, 'isco alarcon')
        self.emp2.first = 'alvaro'
        self.emp2.last = 'morata'
        self.assertEqual(self.emp2.full_name, 'alvaro morata')

    def test_pay(self):
        print('test_pay\n')
        self.assertEqual(self.emp1.apply_raise, 6000)
        self.emp1.pay_raise = 1.5
        self.assertEqual(self.emp1.apply_raise, 9000)

        self.assertEqual(self.emp2.apply_raise, 10000)
        self.emp2.pay_raise = .5
        self.assertEqual(self.emp2.apply_raise, 5000)


if __name__ == '__main__':
    unittest.main()

# here  v text whether value of apply_raise and pay are equal.
# here setUp runs before each test and tearDown method runs after each test.
# order will be like
#     setUp
#     testmethod
#     teardown
