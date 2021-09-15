"""
Create a program to secure an existing password by replacing a set of characters with the corresponding 
'secure-password' characters (provided as a tuple)
"""
SECURE = (('s', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('i', '1'), ('I', '|'))

def securePasssword(password):
    for a, b in SECURE:
        password = password.replace(a, b)
    return password


if __name__=="__main__":
    password = input("Enter your password: ")
    password = securePasssword(password)
    print(f"Your secure password is {password}")
