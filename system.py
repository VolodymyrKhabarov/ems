"""
A very advanced employee management system
"""

import logging
from dataclasses import dataclass

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

    @property
    def fullname(self):
        """Return employe's full name"""

        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.fullname

    def take_payout_holiday(self):
        """Take a payout vacation"""

        if self.vacation_days < 5:
            msg = f"{self} have not enough vacation days. " \
                  f"Remaining days: %d. Requested: %d" % (self.vacation_days, 5)
            raise ValueError(msg)
        self.vacation_days -= 5
        msg = f"Taking a payout vacation. Remaining vacation days: %d " % (self.vacation_days)
        logger.info(msg)

    def take_single_holiday(self):
        """Take a single holiday"""

        if self.vacation_days < 1:
            msg = f"{self} have not enough vacation days. " \
                  f"Remaining days: %d. Requested: %d" % (self.vacation_days, 1)
            raise ValueError(msg)
        self.vacation_days -= 1
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


# noinspection PyTypeChecker
@dataclass
class SalariedEmployee(Employee):
    """Represents employees who are paid on a monthly salary base"""

    salary: int = 5000


# noinspection PyTypeChecker
class Company:
    """A company representation"""

    def __init__(self, title: str, employees: list[Employee] = None):
        self.title = title
        self.employees = employees or []

    def get_ceos(self) -> list[Employee]:
        """Return employees list with role of CEO"""

        result = []
        for employee in self.employees:
            if employee.role == "CEO":
                result.append(employee)
        return result

    def get_managers(self) -> list[Employee]:
        """Return employees list with role of manager"""

        result = []
        for employee in self.employees:
            if employee.role == "manager":
                result.append(employee)
        return result

    def get_developers(self) -> list[Employee]:
        """Return employees list with role of developer"""

        result = []
        for employee in self.employees:
            if employee.role == "dev":
                result.append(employee)
        return result

    @staticmethod
    def pay(employee: Employee) -> int:
        """Pay to employee"""

        if isinstance(employee, SalariedEmployee):
            msg = f"Paying monthly salary of {employee.salary} to {employee}"
            logger.info(msg)  # виправив тут
            return employee.salary

        if isinstance(employee, HourlyEmployee):
            msg = f"Paying {employee} hourly rate of {employee.hourly_rate} for " \
                  f"{employee.amount} hours"
            logger.info(msg)
            return round(employee.amount * employee.hourly_rate, 2)

        msg = "Очікується екземпляр класу SalariedEmployee або HourlyEmployee"
        raise TypeError(msg)

    def pay_all(self) -> int:
        """Pay all the employees in this company"""

        result = 0

        for employee in self.employees:
            result += Company.pay(employee)

        return result
