# -----Writing And Appending To A File-----
f = open("nikhil1.txt", "w")
f.write("Nikhil bhai bhut acche hain\n")
f.close()

f = open("nikhil1.txt", "a")
a = f.write("Nikhil bhai bhut acche hain\n")
print(a)
f.close()

f = open("nikhil2.txt", "r+")
print(f.read())
f.write("Nikhil bhai bhut acche hain\n")
f.write("Thank you\n")
f.close()
