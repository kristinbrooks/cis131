"""
    script: project1Employees.py
    action: a menu-driven application that reads in employee data and displays reports based on the chosen menu option
    author: Kristin Brooks
    date:   07/12/26
"""
from abc import ABC, abstractmethod
from datetime import date


class Person(ABC):
    """An abstract person class"""
    def __init__(self, first_name, last_name, id_number, email_address, phone_number):
        """Initialize a person's attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self._id_number = self._convert_and_validate_id(id_number)
        self.email_address = email_address
        self.phone_number = phone_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = self._validate_non_empty_string(first_name, 'First name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = self._validate_non_empty_string(last_name, 'Last name')

    @property
    def id_number(self):
        return self._id_number

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Validates the string and checks the for valid email address formatting"""
        email_address = self._validate_non_empty_string(email_address, 'Email address')
        if email_address.count('@') != 1:
            raise ValueError('Invalid email address: Email address must contain a single @.')
        local, domain = email_address.split('@')
        if not local or not domain:
            raise ValueError('Invalid email address: Email address must have text before and after the @.')
        self._email_address = email_address

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Validates the string and checks the length of the phone number"""
        phone_number = self._validate_non_empty_string(phone_number, 'Phone number')
        if len(phone_number) != 12:
            raise ValueError('Invalid phone number: Phone number must be 12 characters long.')
        self._phone_number = phone_number

    @staticmethod
    def _convert_and_validate_id(id_number):
        """Converts the id number to an integer and checks that it is a 4-digit number"""
        try:
            id_number = int(id_number)
        except (TypeError, ValueError):
            raise ValueError('Invalid ID number: ID number must be an integer.') from None
        if not 1000 <= id_number <= 9999:
            raise ValueError('Invalid ID number: ID must be 4 digits')
        return id_number

    @staticmethod
    def _validate_non_empty_string(attribute, error_field_name):
        """Validates that the attribute both is a string and not an empty string."""
        if not isinstance(attribute, str):
            raise ValueError(f'Invalid {error_field_name}: {error_field_name} must be a string.')
        attribute = attribute.strip()
        if not attribute:
            raise ValueError(f'Invalid {error_field_name}: {error_field_name} must not be empty.')
        return attribute

    @abstractmethod
    def __str__(self):
        """Abstract method to be overridden in subclasses"""
        raise NotImplementedError('This method should not be called. It should be overridden in the subclasses.')

    def __repr__(self):
        """Representation of a person object"""
        return (f'Person(first_name={self.first_name!r}, '
                f'last_name={self.last_name!r}, '
                f'id_number={self._id_number!r}, '
                f'email_address={self.email_address!r}, '
                f'phone_number={self.phone_number!r})')


class Employee(Person):
    """An employee class for faculty and staff"""
    # class variables
    role_dictionary = {'001': 'Staff', '002': 'Faculty'}
    classification_dictionary = {'001': 'Full', '002': 'Part'}

    def __init__(self, first_name, last_name, id_number, email_address, phone_number, hire_date,
                 role_person, classification_person, annual_salary):
        """Initialize an employee's attributes"""
        super().__init__(first_name, last_name, id_number, email_address, phone_number)
        self._hire_date = self._convert_and_validate_hire_date(hire_date)
        self.role_person = role_person
        self.classification_person = classification_person
        self.annual_salary = annual_salary

    @property
    def hire_date(self):
        return self._hire_date

    @property
    def role_person(self):
        return self._role_person

    @role_person.setter
    def role_person(self, role_person):
        """Checks that the role is in the class variable dictionary"""
        if role_person not in self.role_dictionary:
            raise ValueError('Invalid role: Role must be in the role dictionary.')
        self._role_person = role_person

    @property
    def classification_person(self):
        return self._classification_person

    @classification_person.setter
    def classification_person(self, classification_person):
        """Checks that the classification is in the class variable dictionary"""
        if classification_person not in self.classification_dictionary:
            raise ValueError('Invalid classification: Classification must be in the classification dictionary.')
        self._classification_person = classification_person

    @property
    def annual_salary(self):
        return self._annual_salary

    @annual_salary.setter
    def annual_salary(self, annual_salary):
        """Converts annual salary to a float, checks it's non-negative, and stores it with 2 decimal places."""
        try:
            annual_salary = float(annual_salary)
        except (TypeError, ValueError):
            raise ValueError('Invalid annual salary: Annual salary must be a float.') from None
        if annual_salary < 0:
            raise ValueError('Invalid annual salary: Annual salary must be non-negative.')
        self._annual_salary = round(annual_salary, 2)

    @staticmethod
    def _convert_and_validate_hire_date(hire_date):
        """Converts hire date string to a datetime object"""
        try:
            parts = hire_date.split('/')
        except AttributeError:
            raise ValueError('Invalid hire date: Hire date must be a string.') from None
        if len(parts) != 3:
            raise ValueError('Invalid hire date: Hire date must be in the format Month/Day/Year.')
        month, day, year = parts
        try:
            month = int(month)
            day = int(day)
            year = int(year)
            return date(year, month, day)
        except (TypeError, ValueError):
            raise ValueError('Invalid hire date: Hire date must be numbers and from a valid date.') from None

    def __str__(self):
        """Represent an employee as a string"""
        return (f'{self.first_name} {self.last_name}\n'
                f'ID: {self.id_number}\n'
                f'Email address: {self.email_address}\n'
                f'Phone number: {self.phone_number}\n'
                f'Hire date: {self.hire_date.month}/{self.hire_date.day}/{self.hire_date.year}\n'
                f'Role: {self.role_dictionary[self.role_person]}\n'
                f'Classification: {self.classification_dictionary[self.classification_person]}\n'
                f'Annual salary: {self.annual_salary:.2f}')

    def __repr__(self):
        """Representation of an employee object"""
        return (f'Employee(first_name={self.first_name!r}, '
                f'last_name={self.last_name!r}, '
                f'id_number={self._id_number!r}, '
                f'email_address={self.email_address!r}, '
                f'phone_number={self.phone_number!r}, '
                f'hire_date={self._hire_date!r}, '
                f'role_person={self.role_person!r}, '
                f'classification_person={self.classification_person!r}, '
                f'annual_salary={self.annual_salary!r})')


def get_key_from_value(dictionary, value):
    """Takes the value from the employee text and returns the key for storage"""
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def get_employees(filename):
    """Takes the employee text file, reads in and creates Employee objects, and returns the employees list"""
    try:
        with open(filename, mode='r') as employee_file:
            try:
                next(employee_file)
            except StopIteration:
                raise ValueError('Employee text file is empty.') from None
            for line in employee_file:
                if not line.strip():
                    continue
            # finish this

    except FileNotFoundError:
        raise ValueError('The employee text file was not found.') from None
