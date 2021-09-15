"""Smart Calculator: Munna"""
import re

def Add(num1, num2):
    return num1 + num2


def Sub(num1, num2):
    return num1 - num2


def Mul(num1, num2):
    return num1 * num2


def Div(num1, num2):
    return num1 / num2


def LCM(num1, num2):
    temp = max(num1, num2)
    while True:
        if temp % num1 == 0 and temp % num2 == 0:
            break
        temp += 1
    return temp


def HCF(num1, num2):
    temp = min(num1, num2)
    while True:
        if num1 % temp == 0 and num2 % temp == 0:
            break
        temp -= 1
    return temp


if __name__ == "__main__":
    searchDict = {
        "ADD": ['add', 'sum', '+'],
        "SUB": ['subtract', 'difference', '-'],
        "MUL": ['multiply', 'product', '*'],
        "DIV": ['divide', 'upon', '/'],
        "LCM": ['lcm', 'lowest common multiple'],
        "HCF": ['hcf', 'highest common factor', 'gcd', 'greatest common divisor'],
        "NAME": ['name', 'who are you'],
        "EXIT": ['exit', 'quit', 'end']
    }
    print("Welcome to 'Smart Calculator'\nThis is Munna, what can I do for you?")
    while True:
        query = input("\nQuery: ")
        to_perform = "None"
        for key in searchDict.keys():
            for operation in searchDict[key]:
                if operation in query.lower():
                    to_perform = key
                    break
        if to_perform in ["ADD", "SUB", "MUL", "DIV", "LCM", "HCF"]:
            numbersList = re.findall(r'\d+', query)
            if len(numbersList) in [0, 1]:
                print("Please enter enough numbers to perform the operation")
                continue
        if to_perform == "ADD":
            print(f"{numbersList[0]} + {numbersList[1]} = {Add(int(numbersList[0]), int(numbersList[1]))}")
        
        elif to_perform == "SUB":
            print(f"{numbersList[0]} - {numbersList[1]} = {Sub(int(numbersList[0]), int(numbersList[1]))}")
        
        elif to_perform == "MUL":
            print(f"{numbersList[0]} * {numbersList[1]} = {Mul(int(numbersList[0]), int(numbersList[1]))}")
        
        elif to_perform == "DIV":
            try:
                print(f"{numbersList[0]} / {numbersList[1]} = {Div(int(numbersList[0]), int(numbersList[1]))}")
            except ZeroDivisionError:
                print("Can't divide by zero.")

        elif to_perform == "LCM":
            print(f"LCM({numbersList[0]}, {numbersList[1]}) = {LCM(int(numbersList[0]), int(numbersList[1]))}")
        
        elif to_perform == "HCF":
            print(f"HCF({numbersList[0]}, {numbersList[1]}) = {HCF(int(numbersList[0]), int(numbersList[1]))}")
        
        elif to_perform == "NAME":
            print("My name is Munna")
        
        elif to_perform == "EXIT":
            print("Thanks for visiting!!!")
            break
        else:
            print("Can't recognize the operation, please try again!!!")
