# -----Function Caching-----
import time
from functools import lru_cache


@lru_cache(maxsize=5)
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return 0


if __name__ == '__main__':
    print("Now running some task")
    some_work(3)
    some_work(2)
    some_work(1)
    some_work(5)
    print("Done... Calling again")
    some_work(3)
    print("Called again")
