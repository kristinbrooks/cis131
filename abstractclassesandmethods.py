"""
    script: abstractclassesandmethods.py
    action: an employee payroll system with an abstract base class
    author: Kristin Brooks
    date:   07/09/26
"""
from abc import ABC, abstractmethod
from decimal import Decimal


class Employee(ABC):
    """An abstract employee."""
    def __init__(self, first_name, last_name, ssn):
        """Initialize an employee's attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @abstractmethod
    def earnings(self):
        raise NotImplementedError('This method should not be called. It should be overridden in the subclasses.')

    def __repr__(self):
        """Represent an employee as a string."""
        return (f'Employee: {self.first_name} {self.last_name}\n' +
                f'social security number: {self.ssn}')


class SalariedEmployee(Employee):
    """An employee who earns a weekly salary."""
    def __init__(self, first_name, last_name, ssn, weekly_salary):
        """Initialize a salaried employee's attributes."""
        super().__init__(first_name, last_name, ssn)
        self.weekly_salary = weekly_salary

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, weekly_salary):
        """Set weekly salary or raise ValueError if invalid."""
        if weekly_salary < Decimal('0.00'):
            raise ValueError('Weekly salary must be greater than or equal to 0.')

        self._weekly_salary = weekly_salary

    def earnings(self):
        """Return the employee's weekly earnings."""
        return self.weekly_salary

    def __repr__(self):
        """Represent a salaried employee as a string."""
        return (f'Salaried' + super().__repr__() +
                f'\nweekly salary: {self.weekly_salary}')


class HourlyEmployee(Employee):
    """An employee who earns an hourly wage."""
    def __init__(self, first_name, last_name, ssn, hours, wages):
        """Initialize an hourly employee's attributes."""
        super().__init__(first_name, last_name, ssn)
        self.hours = hours
        self.wages = wages

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Set hours worked or raise ValueError if invalid"""
        if hours < 0 or hours > 168:
            raise ValueError('Hours worked must be between 0 and 168')

        self._hours = hours

    @property
    def wages(self):
        return self._wages

    @wages.setter
    def wages(self, wages):
        """Set hourly wage or raise ValueError if invalid"""
        if wages < Decimal('0.00'):
            raise ValueError('Hourly wage must be greater than or equal to 0.')

        self._wages = wages

    def earnings(self):
        """Return the weekly earnings."""
        if self.hours > 40:
            overtime_hours = self.hours - 40
            overtime_pay = overtime_hours * (self.wages * Decimal('1.5'))
            return 40 * self.wages + overtime_pay
        else:
            return self.hours * self.wages

    def __repr__(self):
        """Represent an hourly employee as a string."""
        return (f'Hourly' + super().__repr__() +
                f'\nhours worked: {self.hours}' +
                f'\nhourly wage: {self.wages}')

# testing the classes
if __name__ == '__main__':
    try:
        employee1 = Employee('John', 'Smith', '123-45-6789')
        print(employee1)
    except TypeError as e:
        print(f'TypeError: {e}')
    print()
    employee2 = SalariedEmployee('Jane', 'Doe', '987-65-4321', Decimal('1200.00'))
    print(employee2)
    print(f'weekly earnings: {employee2.earnings()}')
    print()
    employee3 = HourlyEmployee('Sally', 'Parker', '135-79-2468', 40, Decimal('25.00'))
    print(employee3)
    print(f'weekly earnings: {employee3.earnings()}')
    print()
    employee4 = HourlyEmployee('Jim', 'Green', '975-31-8642', 45, Decimal('25.00'))
    print(employee4)
    print(f'weekly earnings: {employee4.earnings()}')
    print()
    # put employees in a list and polymorphically process each
    employees = [employee2, employee3, employee4]
    for employee in employees:
        print(employee)
        print(f'weekly earnings: {employee.earnings()}')
        print()
