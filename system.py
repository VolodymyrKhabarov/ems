"""
A very advanced employee management system
"""

import logging
from dataclasses import dataclass

FIXED_PAYOUT_DAYS = 5
SINGLE_HOLIDAY = 1


class PayoutHolidayError(Exception):
    def __init__(self, fullname, vacation_days):
        self.fullname = fullname
        self.vacation_days = vacation_days

    def __str__(self):
        return f"{self.fullname} have not enough vacation days. " \
               f"Remaining days: %d. Requested: %d" % (self.vacation_days, FIXED_PAYOUT_DAYS)


class SingleHolidayError(Exception):
    def __init__(self, fullname, vacation_days):
        self.fullname = fullname
        self.vacation_days = vacation_days

    def __str__(self):
        return f"{self.fullname} have not enough vacation days. " \
               f"Remaining days: %d. Requested: %d" % (self.vacation_days, SINGLE_HOLIDAY)


class PayAllError(Exception):
    def __init__(self, title, bank_account, employee):
        self.title = title
        self.bank_account = bank_account
        self.employee = employee

    def __str__(self):
        return f"{self.title} does not have enough money in its bank account. " \
               f"Remaining balance: %d. Requested: %d" % (self.bank_account, self.employee.pay())


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# noinspection PyTypeChecker
@dataclass
class Employee:
    """Basic employee representation"""

    first_name: str
    last_name: str
    role: str
    vacation_days: int = 25
    card: int = 0

    @property
    def fullname(self):
        """Return employe's full name"""

        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.fullname

    def take_payout_holiday(self):
        """Take a payout vacation"""
        if self.vacation_days < FIXED_PAYOUT_DAYS:
            raise PayoutHolidayError(self.fullname, self.vacation_days)
        self.vacation_days -= FIXED_PAYOUT_DAYS
        msg = f"Taking a payout vacation. Remaining vacation days: %d " % (self.vacation_days)
        logger.info(msg)

    def take_single_holiday(self):
        """Take a single holiday"""
        if self.vacation_days < SINGLE_HOLIDAY:
            raise SingleHolidayError(self.fullname, self.vacation_days)
        self.vacation_days -= SINGLE_HOLIDAY
        msg = "Taking a single holiday. Remaining vacation days: %d " % (self.vacation_days)
        logger.info(msg)


# noinspection PyTypeChecker
@dataclass
class HourlyEmployee(Employee):
    """Represents employees who are paid on worked hours base"""

    amount: int = 0
    hourly_rate: int = 50

    def log_work(self, hours: int) -> None:
        """Log working hours"""

        self.amount += hours

    def pay(self):
        """Pay to employee"""
        msg = f"Paying {self.fullname} hourly rate of {self.hourly_rate} for " \
              f"{self.amount} hours"
        logger.info(msg)
        return round(self.amount * self.hourly_rate, 2)


# noinspection PyTypeChecker
@dataclass
class SalariedEmployee(Employee):
    """Represents employees who are paid on a monthly salary base"""

    salary: int = 5000

    def pay(self):
        """Pay to employee"""
        msg = f"Paying monthly salary of {self.salary} to {self.fullname}"
        logger.info(msg)  # виправив тут
        return self.salary


# noinspection PyTypeChecker
class Company:
    """A company representation"""

    def __init__(self, title: str, bank_account: float, employees: list[Employee] = None):
        self.title = title
        self.employees = employees or []
        self.bank_account = bank_account

    def get_employees(self, role):
        return [employee for employee in self.employees if employee.role == role]

    def pay_all(self):
        """Pay all the employees in this company"""

        for employee in self.employees:
            if self.bank_account < employee.pay():
                raise PayAllError(self.title, self.bank_account, employee)
            self.bank_account -= employee.pay()
            employee.card += employee.pay()
