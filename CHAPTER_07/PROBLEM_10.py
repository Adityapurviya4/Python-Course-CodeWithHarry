# 9. Write a program to print the following star pattern.
# * * *
# *   *
# * * *

usernumber = int(input("enter your number to print pattern: "))

for i in range(usernumber):
    for j in range(usernumber):
        if(i == 0 or i == usernumber - 1 or j == 0 or j == usernumber - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()