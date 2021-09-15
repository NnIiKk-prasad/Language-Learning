# Practice Problem 8 - Fake Multiplication Table
import random


def rohanMultipliction(number):
    wrong = random.randint(1, 8)
    table = [number * i for i in range(1, 11)]
    table[wrong] = random.randint(number * wrong, number * (wrong + 1))
    return table


def isCorrect(table, number):
    for i in range(1, 11):
        if table[i - 1] != number * i:
            return i - 1
    return None


if __name__ == '__main__':
    print("-----Multiplication Table-----")
    try:
        number = int(input("Enter a number: "))

        my_table = rohanMultipliction(number)
        print(f"Table of {number} is: {my_table}")

        wrong_index = isCorrect(my_table, number)
        if wrong_index is not None:
            print(f"Table is wrong at index {wrong_index}.")
    except ValueError:
        print("Enter numbers only!")
