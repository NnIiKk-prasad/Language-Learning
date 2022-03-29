# -----While loops-----
i = 0
while i <= 45:
    print(i, end=" ")
    i = i + 1
print("\n")

j = 0
while True:
    if j < 5:
        j = j + 1
        continue
    print(j, end=" ")
    if j == 45:
        break
    j = j + 1
