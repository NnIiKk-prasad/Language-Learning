# -----Class Methods & Alternative Constructor-----
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

    @classmethod
    def from_dash(cls, string):  # Alternative Constructor
        # param = _string.split("-")
        # return cls(param[0], param[1], param[2])
        return cls(*string.split("-"))


rohan = Employee("Rohan", 40000, "Instructor")
harry = Employee("Harry", 45000, "Manager")

rohan.change_leaves(12)   # can change class attribute with class method
print(rohan.no_of_leaves)
print(harry.no_of_leaves)

karan = Employee.from_dash("Karan-15000-Intern")
print(karan.print_details())
