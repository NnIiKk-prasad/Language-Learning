# -----External & Built In Modules-----
import random   # built-in module
import file2    # external module

random_num = random.randint(-4, 0)
print(random_num)
rand = random.random() * 100
print(rand)
lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
ch = random.choice(lst)
print(ch)

print(file2.a)
file2.print_joke("This is me.")
