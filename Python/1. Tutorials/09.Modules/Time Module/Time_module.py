# -----Time module-----
import time

# time.time() returns the current time in milliseconds since midnight, January 1, 1970 GMT (the Unix time)
print(time.time())
print(time.localtime(time.time()))

for j in range(5):
    time.sleep(2)
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)


# -------------Exercise--------------------
def for_loop_time():
    init = time.time()
    for i in range(45):
        print("Nikhil is a good boy")
    loop_time = time.time() - init
    return loop_time


def while_loop_time():
    init = time.time()
    i = 0
    while i < 45:
        print("Nikhil is a good boy")
        i += 1
    loop_time = time.time() - init
    return loop_time


for_count = 0
while_count = 0

for j in range(150):
    for_count = for_count + for_loop_time()
    while_count = while_count + while_loop_time()

average_for_loop_time = for_count / 150
average_while_loop_time = while_count / 150

print(f"For loop takes {average_for_loop_time} seconds")
print(f"While loop takes {average_while_loop_time} seconds")
