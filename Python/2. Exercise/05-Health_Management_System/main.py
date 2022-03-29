# -----Health Management System-----
from datetime import datetime

# customizable variables
client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
log_list = {1: "Food", 2: "Exercise"}


def log(client):
    for key, value in log_list.items():
        print("Press", key, "to log for", value)
    ch = int(input("Enter your choice: "))
    data = input("Type here:\n")
    if client == 1 and ch == 1:
        with open("harry_food.txt", "a") as f:
            f.write(f"[{datetime.now()}] : {data}\n")
    elif client == 1 and ch == 2:
        with open("harry_ex.txt", "a") as f:
            f.write(f"[{datetime.now()}] : {data}\n")
    elif client == 2 and ch == 1:
        with open("rohan_food.txt", "a") as f:
            f.write(f"[{datetime.now()}] : {data}\n")
    elif client == 2 and ch == 2:
        with open("rohan_ex.txt", "a") as f:
            f.write(f"[{datetime.now()}] : {data}\n")
    elif client == 3 and ch == 1:
        with open("hammad_food.txt", "a") as f:
            f.write(f"[{datetime.now()}] : {data}\n")
    elif client == 3 and ch == 2:
        with open("hammad_ex.txt", "a") as f:
            f.write(f"[{datetime.now()}] : {data}\n")
    else:
        print("Invalid Input")
        return 0
    print("Successfully written")
    return 0


def retrieve(client):
    for key, value in log_list.items():
        print("Press", key, "to retrieve", value, "details")
    ch = int(input("Enter your choice: "))
    print("Here's your log:")
    if client == 1 and ch == 1:
        with open("harry_food.txt") as f:
            for line in f:
                print(line, end="")
    elif client == 1 and ch == 2:
        with open("hammad_ex.txt") as f:
            for line in f:
                print(line, end="")
    elif client == 2 and ch == 1:
        with open("rohan_food.txt") as f:
            for line in f:
                print(line, end="")
    elif client == 2 and ch == 2:
        with open("rohan_ex.txt") as f:
            for line in f:
                print(line, end="")
    elif client == 3 and ch == 1:
        with open("hammad_food.txt") as f:
            for line in f:
                print(line, end="")
    elif client == 3 and ch == 2:
        with open("hammad_ex.txt") as f:
            for line in f:
                print(line, end="")
    else:
        print("Invalid Input")
        return 0
    return 0


if __name__ == '__main__':
    try:
        print("----Health Management System----")
        print("\nSelect client name:")
        for s_no, name in client_list.items():
            print("Press", s_no, "for", name)
        user_ch = int(input("Your your choice: "))
        print(f"\nWelcome {client_list[user_ch]}")
        print("Press 1 for Log or press 2 for Retrieve:")
        op = input("Enter your choice: ")
        if op == '1':
            log(user_ch)
        elif op == '2':
            retrieve(user_ch)
        else:
            print("Invalid Input")
    except Exception as e:
        print("Invalid Input:", e)
