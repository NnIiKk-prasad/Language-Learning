# -----Decorators-----
def dec1(func):
    def now_exec():
        print("Executing now")
        func()
        print("Executed")
    return now_exec


@dec1
def who_is_nikhil():
    print("Nikhil is a good boy")


# who_is_nikhil = dec1(who_is_nikhil)
who_is_nikhil()
