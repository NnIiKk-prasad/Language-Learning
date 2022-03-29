# -----Operator Overloading & Dunder Methods-----
class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    def __add__(self, other):   # Operator overloading
        return self.salary + other.salary

    def __truediv__(self, other):   # Operator overloading
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}."


emp1 = Employee("Harry", 35000, "Programmer")
emp2 = Employee("Rohan", 10000, "Cleaner")

print(emp1 + emp2)
print(emp1 / emp2)
print(emp1)
print(str(emp1))
print(repr(emp1))
