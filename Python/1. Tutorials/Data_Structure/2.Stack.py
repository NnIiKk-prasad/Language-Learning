# -----Stack implementation using Linked List-----
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.start = None

    def push(self, value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            self.start = newNode
            newNode.next = temp
        print("Value pushed sucessfully!")

    def pop(self):
        if self.start == None:
            print("Stack is underflow")
        else:
            temp = self.start
            self.start = self.start.next
            print(f"Popped value is {temp.data}")

    def peek(self):
        if self.start == None:
            print("Stack is empty")
        else:
            print(f"Top value is {self.start.data}")

    def removeStack(self):
        self.start = None
        print("Stack removed sucessfully!")


def menu():
    print("\nPress '1' to push value to the stack"
          "\nPress '2' to pop value from the stack"
          "\nPress '3' to peek the stack"
          "\nPress '4' to remove the stack"
          "\nPress '5' to exit")
    choice = input("Enter your choice: ")
    return choice


if __name__ == '__main__':
    print("-----Stack Program-----")
    myStack = Stack()
    while True:
        ch = menu()
        if ch == '1':
            val = input("Enter a value: ")
            myStack.push(val)
        elif ch == '2':
            myStack.pop()
        elif ch == '3':
            myStack.peek()
        elif ch == '4':
            myStack.removeStack()
        elif ch == '5':
            break
        else:
            print("Invalid choice")
