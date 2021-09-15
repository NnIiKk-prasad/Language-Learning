# -----Multiple Inheritance-----
class Employee:
    var = 8
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


class Player:
    var = 9
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_details(self):
        return f"Name is {self.name}. Game is {self.game}."


class CoolProgrammer(Employee, Player):
    language = "C++"

    def print_language(self):
        print(self.language)


rohan = Employee("Rohan", 40000, "Instructor")
harry = Employee("Harry", 45000, "Manager")

rahul = Player("Rahul", ["Cricket"])
karan = CoolProgrammer("Karan", 25000, "Intern")

print(karan.print_details())
karan.print_language()
print(karan.var)
