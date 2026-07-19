"""
    script: project3.py
    action: a menu-driven application that reads in employee and student data and displays reports based on
            the chosen menu option
    author: Kristin Brooks
    date:   07/19/26
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
                f'id_number={self.id_number!r}, '
                f'email_address={self.email_address!r}, '
                f'phone_number={self.phone_number!r})')


class Employee(Person):
    """An employee class for faculty and staff inheriting from the abstract Person class"""
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
                f'id_number={self.id_number!r}, '
                f'email_address={self.email_address!r}, '
                f'phone_number={self.phone_number!r}, '
                f'hire_date={self.hire_date}, '
                f'role_person={self.role_person!r}, '
                f'classification_person={self.classification_person!r}, '
                f'annual_salary={self.annual_salary!r})')


class Student(Person):
    """A student class inheriting from the abstract Person class"""
    # class variable
    course_name_list = ['Art', 'Latin', 'Greek', 'Science', 'Mathematics', 'Painting', 'Sculpting']

    def __init__(self,first_name, last_name, id_number, email_address, phone_number):
        """Initialize a student's attributes"""
        super().__init__(first_name, last_name, id_number, email_address, phone_number)
        self.courses_student_dict = {}

    @staticmethod
    def _convert_and_validate_score(score):
        """Converts a score to an integer and checks it's in range"""
        try:
            score = int(score)
        except (TypeError, ValueError):
            raise ValueError('Invalid score: Score must be an integer.') from None
        if score <= 0 or score > 100:
            raise ValueError('Invalid score: Score must be between 1 and 100.')
        return score

    def add_score(self, course, score):
        """Validates a course and score and adds it to the student's course dictionary"""
        score = self._convert_and_validate_score(score)
        if course not in self.course_name_list:
            raise ValueError('Invalid course: Course must be in the course name list.')
        self.courses_student_dict[course] = score

    def get_student_academics(self):
        """Returns a list of student's name, id, and academic scores"""
        courses = ['Art', 'Greek', 'Latin', 'Science', 'Mathematics']
        student_academics = [self.last_name, self.first_name, self.id_number]
        for course in courses:
            student_academics.append(self.courses_student_dict.get(course,'N/A'))
        return student_academics

    def __str__(self):
        """Represent a student as a string"""
        return (f'{self.first_name} {self.last_name}\n'
                f'ID: {self.id_number}\n'
                f'Email address: {self.email_address}\n'
                f'Phone number: {self.phone_number}')

    def __repr__(self):
        """Representation of a student object"""
        return (f'Student(first_name={self.first_name!r}, '
                f'last_name={self.last_name!r}, '
                f'id_number={self.id_number!r}, '
                f'email_address={self.email_address!r}, '
                f'phone_number={self.phone_number!r})')

# helper function
def get_key_from_value(dictionary, value):
    """Takes the value from the employee text and returns the key for storage"""
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

# functions getting data from files
def get_employees(filename):
    """Takes the employee text file, reads in and creates Employee objects, and returns the employees list"""
    try:
        with open(filename, mode='r') as employee_file:
            try:
                # skip header line
                next(employee_file)
            except StopIteration:
                raise ValueError('Employee text file is empty.') from None
            employee_list = []
            for line in employee_file:
                # skip blank lines
                if not line.strip():
                    continue
                try:
                    # read in a line and unpack into variables
                    last_name, first_name, id_number, email_address, phone_number, hire_date, classification_value, role_value, annual_salary = line.split()
                    # get the dictionary keys
                    classification_key = get_key_from_value(Employee.classification_dictionary, classification_value)
                    role_key = get_key_from_value(Employee.role_dictionary, role_value)
                    if classification_key is None or role_key is None:
                        continue
                    # Create an Employee object
                    employee = Employee(first_name=first_name, last_name=last_name, id_number=id_number, email_address=email_address,
                                    phone_number=phone_number, hire_date=hire_date, role_person=role_key,
                                    classification_person=classification_key, annual_salary=annual_salary)
                    # add the employee to the list
                    employee_list.append(employee)
                    print(f'Added employee {first_name} {last_name}...')
                except ValueError:
                    continue
            return employee_list
    except FileNotFoundError:
        raise ValueError('The employee text file was not found.') from None

def get_students(filename):
    """Takes the students text file, reads in and creates Student objects, and returns the students list"""
    try:
        with open(filename, mode='r') as student_file:
            try:
                # skip header line
                next(student_file)
            except StopIteration:
                raise ValueError('Student text file is empty.') from None
            student_list = []
            for line in student_file:
                # skip blank lines
                if not line.strip():
                    continue
                try:
                    # read in a line and unpack into variables
                    last_name, first_name, id_number, email_address, phone_number = line.split()
                    # create a Student object
                    student = Student(first_name=first_name, last_name=last_name, id_number=id_number,
                                      email_address=email_address, phone_number=phone_number)
                    # add the student to the list
                    student_list.append(student)
                    print(f'Added student {first_name} {last_name}...')
                except ValueError:
                    continue
            return student_list
    except FileNotFoundError:
        raise ValueError('The students text file was not found.') from None

def get_student_scores(filename, student_list):
    """Reads in the student scores and adds them to the student's course dictionary"""
    score_columns = ['Art', 'Greek', 'Latin', 'Science', 'Mathematics']
    try:
        with open(filename, mode='r') as student_scores_file:
            try:
                # skip header line
                next(student_scores_file)
            except StopIteration:
                raise ValueError('Student scores file is empty.') from None
            for line in student_scores_file:
                # skip blank lines
                if not line.strip():
                    continue
                try:
                    # read in line and unpack into variables
                    id_number, *score_values = line.split()
                    try:
                        id_number = int(id_number)
                    except (TypeError, ValueError):
                        raise ValueError('Student id file must be a number.') from None
                    # search the student_list for a student with the current id number
                    student = next((s for s in student_list if s.id_number == id_number), None)
                    if student is None:
                        continue
                    # add each score to the student course dictionary
                    for course, score in zip(score_columns, score_values):
                        student.add_score(course, score)
                    print(f'Added scores for {student.first_name} {student.last_name}...')
                except ValueError:
                    continue
            return student_list
    except FileNotFoundError:
        raise ValueError('The student scores file was not found.') from None

# display functions
def display_employee_employment_information(employee_list):
    """Displays the employee employment information"""
    print(f'{"Employee Employment Information":^135}')
    print(f'{"LastName":<16}{"FirstName":<16}{"ID":<10}{"Email":<32}'
          f'{"Phone":<18}{"HireDate":<18}{"Classification":<20}{"Role":<14}{"Salary"}')
    for employee in employee_list:
        hire_date = str(employee.hire_date.month) + '/' + str(employee.hire_date.day) + '/' + str(employee.hire_date.year)
        print(f'{employee.last_name:<16}{employee.first_name:<16}{employee.id_number:<10}'
              f'{employee.email_address:<32}{employee.phone_number:<18}'
              f'{hire_date:<18}{Employee.classification_dictionary[employee.classification_person]:<20}'
              f'{Employee.role_dictionary[employee.role_person]:<14}{employee.annual_salary:.2f}')

def display_employee_contact_information(employee_list):
    """Displays the employee contact information"""
    print(f'{"Employee Contact Information":^75}')
    print(f'{"LastName":<16}{"FirstName":<16}{"ID":<10}{"Email":<32}{"Phone":<18}')
    for employee in employee_list:
        print(f'{employee.last_name:<16}{employee.first_name:<16}{employee.id_number:<10}'
              f'{employee.email_address:<32}{employee.phone_number:<18}')

def display_student_contact_information(student_list):
    """Displays the student contact information"""
    print(f'{"Student Contact Information":^75}')
    print(f'{"LastName":<16}{"FirstName":<16}{"ID":<10}{"Email":<32}{"Phone":<18}')
    for student in student_list:
        print(f'{student.last_name:<16}{student.first_name:<16}{student.id_number:<10}'
              f'{student.email_address:<32}{student.phone_number:<18}')

def display_all_person_contact_information(employee_list, student_list):
    """Displays contact information for all students and employees"""
    person_list = []
    person_list.extend(employee_list)
    person_list.extend(student_list)
    print(f'{"All Person Contact Information":^75}')
    print(f'{"LastName":<16}{"FirstName":<16}{"ID":<10}{"Email":<32}{"Phone":<18}')
    for person in person_list:
        print(f'{person.last_name:<16}{person.first_name:<16}{person.id_number:<10}'
              f'{person.email_address:<32}{person.phone_number:<18}')

def display_student_scores(student_list):
    """Displays the students scores """
    print(f'{"Student Academic Scores":^90}')
    print(f'{"LastName":<16}{"FirstName":<16}{"ID":<10}{"Art":<12}{"Greek":<12}{"Latin":<12}{"Science":<12}{"Mathematics"}')
    for student in student_list:
        last_name, first_name, id_number, art, greek, latin, science, math = student.get_student_academics()
        print(f'{last_name:<16}{first_name:<16}{id_number:<10}{art:<12}{greek:<12}{latin:<12}{science:<12}{math}')

def create_menu(employee_list, student_list):
    """Creates the menu"""
    user_choice = '0'
    while user_choice != '1':
        print()
        print('Please select an option below')
        print()
        print('1. Quit')
        print('2. Display Employee Employment Information')
        print('3. Display Employee Contact Information')
        print('4. Display Student Contact Information')
        print('5. Display All Person Contact Information')
        print('6. Display Student Academic Scores')
        print()
        user_choice = input('>')
        print()
        if user_choice not in ('1', '2', '3', '4', '5', '6'):
            print(f'I am sorry, {user_choice} is not an option.')
            continue
        elif user_choice == '2':
            display_employee_employment_information(employee_list)
        elif user_choice == '3':
            display_employee_contact_information(employee_list)
        elif user_choice == '4':
            display_student_contact_information(student_list)
        elif user_choice == '5':
            display_all_person_contact_information(employee_list, student_list)
        elif user_choice == '6':
            display_student_scores(student_list)
    print('Thank you for using the system.')
    print()
    print('Now exiting the program...')

def main():
    print('Starting application...')
    print()
    print('Adding employees...')
    print()
    try:
        employee_list = get_employees('employees.txt')
    except ValueError as error:
        print(error)
        return
    print()
    print('Adding students...')
    print()
    try:
        student_list = get_students('students.txt')
    except ValueError as error:
        print(error)
        return
    print()
    print('Adding students scores...')
    print()
    try:
        get_student_scores('scores.txt', student_list)
    except ValueError as error:
        print(error)
        return
    print()
    print('Welcome to the College Data System')
    create_menu(employee_list, student_list)


if __name__ == '__main__':
    main()
