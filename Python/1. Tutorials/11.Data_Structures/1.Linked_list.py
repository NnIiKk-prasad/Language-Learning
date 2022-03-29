# -----Linked List-----
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def viewList(self):
        if self.start == None:
            print("Linked list is empty")
        else:
            print("List items are:")
            temp = self.start
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def insertLast(self, value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        print("Added sucessfully!")

    def deleteFirst(self):
        if self.start == None:
            print("Linked list is empty")
        else:
            self.start = self.start.next
            print("Sucessfully deleted!")


def menu():
    print("\nPress '1' to add value to list"
          "\nPress '2' to delete first value"
          "\nPress '3' to view list"
          "\nPress '4' to exit")
    choice = input("Enter your choice: ")
    return choice


if __name__ == '__main__':
    print("-----Linked List Program-----")
    myList = LinkedList()
    while True:
        ch = menu()
        if ch == '1':
            val = input("Enter a value: ")
            myList.insertLast(val)
        elif ch == '2':
            myList.deleteFirst()
        elif ch == '3':
            myList.viewList()
        elif ch == '4':
            break
        else:
            print("Invalid choice")
