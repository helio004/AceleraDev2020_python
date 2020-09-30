from abc import abstractmethod
from abc import ABC


class Department:

    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    def __init__(self, code, name, salary, departament):
        self.code = code
        self.name = name
        self.salary = salary
        self.__departament = departament

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8

    def set_departament(self, departament):
        self.__departament.name = departament

    def get_departament(self):
        return self.__departament.name


class Manager(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.get_sales() * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales
