# -----Else with loops-----
for i in range(10):
    print(i, end=" ")
    if i == 15:
        break
else:
    print("For loop else")


j = 1
while j <= 10:
    print(j, end=" ")
    if j == 5:
        break
    j += 1
else:
    print("While loop else")
