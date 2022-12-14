
from unittest import TestCase, main
import system


class EmsTestCase(TestCase):
    """Represents test cases"""

    def setUp(self) -> None:
        """The setUp() method allow you to define
        instructions that will be executed before each test method"""

        self.person_1 = system.Employee('volodymyr', 'khabarov', 'dev', 5)

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

    def test_initializer_HourlyEmployee(self):
        "This test case verifies initialization of HourlyEmployee class instance."

    def test_log_work(self):
        """This test case verifies 'log_work' method of HourlyEmployee class"""

    def test_inintializer_SalariedEmployee(self):
        "This test case verifies initialization of SalariedEmployee class instance."

    def test_inintializer_Company(self):
        "This test case verifies initialization of Company class instance."

    def test_get_ceos(self):
        """This test case verifies 'get_ceos' method of Company class"""

    def test_get_managers(self):
        """This test case verifies 'get_managers' method of Company class"""

    def test_get_developers(self):
        """This test case verifies 'get_developers' method of Company class"""

    def pay(self):
        """This test case verifies 'pay' method of Company class"""

        hE_CEO = system.HourlyEmployee('Petro', 'Dudu', 'CEO')
        hE_CEO.log_work(7)
        comp = system.Company('Alevel', [hE_CEO])
        self.assertEqual(comp.pay_all(), 350)

    def pay_all(self):
        """This test case verifies 'pay_all' method of Company class"""
        hE_CEO = system.HourlyEmployee('Petro', 'Dudu', 'CEO')
        hE_CEO.log_work(7)
        comp = system.Company('Alevel', [hE_CEO])

if __name__ == '__main__':
    main()