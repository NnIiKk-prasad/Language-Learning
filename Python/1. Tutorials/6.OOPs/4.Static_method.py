# -----Static Method-----
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
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def well_done(string):  # Static Method
        return f"Well done! {string}"


rohan = Employee("Rohan", 40000, "Instructor")
harry = Employee("Harry", 45000, "Manager")
karan = Employee.from_dash("Karan-15000-Intern")

print(karan.well_done("Karan"))
print(Employee.well_done("Karan"))
