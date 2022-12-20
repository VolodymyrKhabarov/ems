"""
This module is for testing the "system" module.
"""

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
        self.he_ceo = system.HourlyEmployee('Petro', 'Dudu', 'CEO')
        self.he_dev = system.HourlyEmployee('Andriy', 'Maksymonko', 'DevOps', hourly_rate=1000)
        self.se_manager = system.SalariedEmployee('vasyl', 'stus', 'manager')
        self.se_manager_2 = system.SalariedEmployee('max', 'petriv', 'manager', salary=10_000)
        self.comp = system.Company('Alevel', 5367.5, [self.he_ceo, self.se_manager])
        self.softserve = system.Company('SoftServe', 10000, [self.person_1])
        self.epam = system.Company('Epam', 0, [self.se_manager])

    def test_initializer_employee(self):
        "This test case verifies initialization of Employee class instance."

        self.assertEqual('volodymyr', self.person_1.first_name)
        self.assertEqual('khabarov', self.person_1.last_name)
        self.assertEqual('dev', self.person_1.role)
        self.assertEqual(5, self.person_1.vacation_days)
        self.assertEqual(0, self.person_1.card)

    def test_fullname(self):
        """This test case verifies 'fullname' method of Employee class"""

        self.assertEqual('volodymyr khabarov', self.person_1.fullname)

    def test_take_payout_holiday(self):
        """This test case verifies 'take_payout_holiday' method of Employee class"""

        self.person_1.take_payout_holiday()
        self.assertEqual(0, self.person_1.vacation_days)

        with self.assertRaises(ValueError) as msg:
            self.person_4.take_payout_holiday()

        self.assertEqual(str(msg.exception),
                         'andrii shevchenko have not enough vacation days. '
                         'Remaining days: 4. Requested: 5')

    def test_take_single_holiday(self):
        """This test case verifies 'take_single_holiday' method of Employee class"""

        self.person_2.take_single_holiday()
        self.assertEqual(0, self.person_2.vacation_days)

        with self.assertRaises(ValueError) as msg:
            self.person_3.take_single_holiday()

        self.assertEqual(str(msg.exception),
                         'svitlana shevchuk have not enough vacation days. '
                         'Remaining days: 0. Requested: 1')

    def test_initializer_hourlyemployee(self):
        "This test case verifies initialization of HourlyEmployee class instance."

        self.assertEqual('Petro', self.he_ceo.first_name)
        self.assertEqual('Dudu', self.he_ceo.last_name)
        self.assertEqual('CEO', self.he_ceo.role)
        self.assertEqual(25, self.he_ceo.vacation_days)
        self.assertEqual(0, self.he_ceo.amount)
        self.assertEqual(50, self.he_ceo.hourly_rate)
        self.assertEqual(1000, self.he_dev.hourly_rate)

    def test_log_work(self):
        """This test case verifies 'log_work' method of HourlyEmployee class"""

        self.he_ceo.log_work(7)
        self.assertEqual(7, self.he_ceo.amount)

    def test_inintializer_salariedemployee(self):
        "This test case verifies initialization of SalariedEmployee class instance."

        self.assertEqual('vasyl', self.se_manager.first_name)
        self.assertEqual('stus', self.se_manager.last_name)
        self.assertEqual('manager', self.se_manager.role)
        self.assertEqual(5000, self.se_manager.salary)
        self.assertEqual(10_000, self.se_manager_2.salary)

    def test_inintializer_company(self):
        "This test case verifies initialization of Company class instance."

        self.assertEqual('Alevel', self.comp.title)
        self.assertEqual([self.he_ceo, self.se_manager], self.comp.employees)
        self.assertEqual(5367.5, self.comp.bank_account)

    def test_get_ceos(self):
        """This test case verifies 'get_ceos' method of Company class"""

        self.assertEqual([self.he_ceo], self.comp.get_ceos())

    def test_get_managers(self):
        """This test case verifies 'get_managers' method of Company class"""

        self.assertEqual([self.se_manager], self.comp.get_managers())

    def test_get_developers(self):
        """This test case verifies 'get_developers' method of Company class"""

        self.assertEqual([], self.comp.get_developers())

    def test_pay(self):
        """This test case verifies 'pay' method of Company class"""

        self.he_ceo.log_work(7.35)
        self.assertEqual(367.5, self.comp.pay(self.he_ceo))
        self.assertEqual(5000, self.comp.pay(self.se_manager))

        with self.assertRaises(TypeError) as msg:
            self.softserve.pay(self.person_1)

        self.assertEqual(str(msg.exception),
                         'Очікується екземпляр класу SalariedEmployee або HourlyEmployee')

    def test_pay_all(self):
        """This test case verifies 'pay_all' method of Company class"""

        self.he_ceo.log_work(7.35)
        self.comp.pay_all()
        self.assertEqual(367.5, self.he_ceo.card)
        self.assertEqual(5000, self.se_manager.card)
        self.assertEqual(0, self.comp.bank_account)

        with self.assertRaises(ValueError) as msg:
            self.epam.pay_all()

        self.assertEqual(str(msg.exception),
                         "Epam does not have enough money in its bank account. " \
                         "Remaining balance: 0. Requested: 5000")


if __name__ == '__main__':
    unittest.main()
