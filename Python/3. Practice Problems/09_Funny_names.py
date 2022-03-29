# Practice Problem 9 - Jumbled Funny Names
import re
import random


def funnyNames(n, nameList):
    for i in range(n):
        rand = random.randint(0, n - 1)
        nameList[i][1] = nameList[rand][1]
    return nameList



if __name__ == "__main__":
    try:
        n = int(input("Enter number of friends: "))
    except ValueError:
        print("Enter numbers only!")
        exit()
    print(f"Enter the names of your {n} friends:")
    nameList = []
    for i in range(n):
        name = input()
        fname_lname = re.split(r"\s", name, 1)
        nameList.append(fname_lname)
    funnyNameList = funnyNames(n, nameList)
    print("\nYour funny names:")
    for fname, lname in funnyNameList:
        print(fname.capitalize(), lname.capitalize())
