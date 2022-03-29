# Practice Problem 5 - Palindromify the list
def nextPalindrome(num):
    num += 1
    while not isPalindrome(num):
        num += 1
    return num


def isPalindrome(num):
    return str(num) == str(num)[::-1]


if __name__ == '__main__':
    try:
        lst = []
        size = int(input("Enter how many numbers you want to add: "))
        for i in range (size):
            lst.append(int(input("Enter the number: ")))
    except ValueError:
        print("Enter numbers only")
    print(f"\nThe list given by you is: {lst}")
    print(f"Output list: {[lst[i] if lst[i] < 10 else nextPalindrome(lst[i]) for i in range(size)]}")
       