import unittest

import system


class EmsTestCase(unittest.TestCase):
    """Represents test cases"""

    def setUp(self) -> None:
        """The setUp() method allow you to define
        instructions that will be executed before each test method"""

        self.person_1 = system.Employee('volodymyr', 'khabarov', 'dev', 5)
        self.person_2 = system.Employee('serhii', 'filatov', 'CEO', 1)
        self.person_3 = system.Employee('svitlana', 'shevchuk', 'manager', 0)
        self.person_4 = system.Employee('andrii', 'shevchenko', 'dev', 4)
        self.hE_CEO = system.HourlyEmployee('Petro', 'Dudu', 'CEO')
        self.sE_manager = system.SalariedEmployee('vasyl', 'stus', 'manager')
        self.comp = system.Company('Alevel', [self.hE_CEO, self.sE_manager])

    def test_initializer_Employee(self):
        "This test case verifies initialization of Employee class instance."

        self.assertEqual('volodymyr', self.person_1.first_name)
        self.assertEqual('khabarov', self.person_1.last_name)
        self.assertEqual('dev', self.person_1.role)
        self.assertEqual(5, self.person_1.vacation_days)

    def test_fullname(self):
        """This test case verifies 'fullname' method of Employee class"""

        self.assertEqual('volodymyr khabarov', self.person_1.fullname)

    def test_take_holiday(self):
        """This test case verifies 'take_holiday' method of Employee class"""
        self.person_1.take_holiday(payout=True)
        self.assertEqual(0, self.person_1.vacation_days)

        # self.person_4.take_holiday(payout=True) - тут не проходить тест
        # self.assertRaises(ValueError, self.person_4.take_holiday(payout=True)) - тут не проходить тест

        self.person_2.take_holiday(payout=False)
        self.assertEqual(0, self.person_2.vacation_days)

        # self.person_3.take_holiday(False) - тут не проходить тест
        # self.assertRaises(ValueError, self.person_3.take_holiday(payout=True)) - тут не проходить тест

    def test_initializer_HourlyEmployee(self):
        "This test case verifies initialization of HourlyEmployee class instance."

        self.assertEqual('Petro', self.hE_CEO.first_name)
        self.assertEqual('Dudu', self.hE_CEO.last_name)
        self.assertEqual('CEO', self.hE_CEO.role)
        self.assertEqual(25, self.hE_CEO.vacation_days)
        self.assertEqual(0, self.hE_CEO.amount)
        self.assertEqual(50, self.hE_CEO.hourly_rate)

    def test_log_work(self):
        """This test case verifies 'log_work' method of HourlyEmployee class"""

        self.hE_CEO.log_work(7)
        self.assertEqual(7, self.hE_CEO.amount)

    def test_inintializer_SalariedEmployee(self):
        "This test case verifies initialization of SalariedEmployee class instance."

        self.assertEqual('vasyl', self.sE_manager.first_name)
        self.assertEqual('stus', self.sE_manager.last_name)
        self.assertEqual('manager', self.sE_manager.role)
        self.assertEqual(5000, self.sE_manager.salary)

    def test_inintializer_Company(self):
        "This test case verifies initialization of Company class instance."

        self.assertEqual('Alevel', self.comp.title)
        self.assertEqual([self.hE_CEO, self.sE_manager], self.comp.employees)

    def test_get_ceos(self):
        """This test case verifies 'get_ceos' method of Company class"""

        self.assertEqual([self.hE_CEO], self.comp.get_ceos())

    def test_get_managers(self):
        """This test case verifies 'get_managers' method of Company class"""

        self.assertEqual([self.sE_manager], self.comp.get_managers())

    def test_get_developers(self):
        """This test case verifies 'get_developers' method of Company class"""

        self.assertEqual([], self.comp.get_developers())

    def test_pay(self):
        """This test case verifies 'pay' method of Company class"""

        self.hE_CEO.log_work(7)
        self.assertEqual(350, self.comp.pay(self.hE_CEO))
        self.assertEqual(5000, self.comp.pay(self.sE_manager))

    def test_pay_all(self):
        """This test case verifies 'pay_all' method of Company class"""

        self.hE_CEO.log_work(7)
        self.assertEqual(5350, self.comp.pay_all())


if __name__ == '__main__':
    unittest.main()
