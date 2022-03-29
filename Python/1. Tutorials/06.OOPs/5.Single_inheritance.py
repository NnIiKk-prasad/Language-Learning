# -----Single Inheritance-----
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
    def well_done(string):
        return f"Well done! {string}"


class Programmer(Employee):
    def __init__(self, name, salary, role, languages):
        super().__init__(name, salary, role)
        self.languages = languages

    def print_programmer(self):
        return f"The programmer name is {self.name}. Salary is {self.salary}. Role is {self.role}. " \
               f"Languages known: {self.languages}"


rohan = Employee("Rohan", 40000, "Instructor")
harry = Employee("Harry", 45000, "Manager")

karan = Programmer("Karan", 15000, "Intern", ["Python"])
rahul = Programmer("Rahul", 20000, "Intern", ["C++", "Python"])

print(karan.print_details())
print(karan.print_programmer())
