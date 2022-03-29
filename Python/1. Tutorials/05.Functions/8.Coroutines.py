# -----Coroutines-----
import time


def searcher():
    # some task taking 4 seconds
    book = "Nikhil is a good boy. Nikhil is the king of the universe. Nikhil is very handsome"
    time.sleep(4)

    while True:
        txt = (yield)
        if txt in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")


if __name__ == '__main__':
    search = searcher()
    print("Loading book...")
    next(search)
    while True:
        text = input("\nEnter text you want to search or enter exit: ")
        if text == 'exit':
            search.close()
            break
        else:
            search.send(text)
