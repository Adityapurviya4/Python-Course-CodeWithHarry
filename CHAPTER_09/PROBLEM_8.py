# 8. Write a program to make a copy of a text file “this.txt”.

with open("this.txt", "r") as f:
    contain = f.read()

with open("this_copy.txt", "w") as f:
    f.write(contain)