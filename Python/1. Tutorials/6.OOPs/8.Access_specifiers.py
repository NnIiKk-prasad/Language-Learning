# Public, Private & Protected Access Specifiers
class Employee:
    no_of_leaves = 8   # Public
    _protect = 9   # Protected
    __private = 10   # Private

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))


emp = Employee("Rohan", 40000, "Instructor")
print(emp.no_of_leaves)
print(emp._protect)
print(emp._Employee__private)
