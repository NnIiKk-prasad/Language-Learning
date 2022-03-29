# -----Self & __init__() (Constructor)-----
class Employee:
    no_of_leaves = 8   # Attribute

    def __init__(self, name, salary, role):   # Constructor
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):   # Method
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}."


rohan = Employee("Rohan", 40000, "Instructor")
harry = Employee("Harry", 45000, "Manager")

print(rohan.print_details())
