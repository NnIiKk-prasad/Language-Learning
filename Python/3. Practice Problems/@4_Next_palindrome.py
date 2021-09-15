# Practice Problem 4 - The Next Palindrome

# def nextPalindrome(num):
#     while True:
#         temp = num + 1
#         temp2 = 0
#         while temp:
#             temp2 = temp2 * 10 + temp % 10
#             temp //= 10
#         if temp2 == num:
#             break
#         num += 1
#     return temp2
def nextPalindrome(num):
    num += 1
    while not isPalindrome(num):
        num += 1
    return num


def isPalindrome(num):
    return str(num) == str(num)[::-1]


if __name__ == '__main__':
    print("-----The Next Palindrome-----")
    try:
        lst = []
        n = int(input("Enter the number of test cases: "))
        print(f"Enter {n} numbers:")
        for i in range(n):
            lst.append(int(input()))
    except ValueError:
        print("Enter numbers only")

    for num in lst:
        print(f"Next Palindrome of {num} is {nextPalindrome(num)}")
