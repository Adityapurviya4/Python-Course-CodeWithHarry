# 7. Write a program to print the following star pattern.
#      *
#    ***
# ***** for n = 4

usernumber = int(input("enter your number print pattern "))

for i in range(1, usernumber+1):
    print("  "*(usernumber-i), end='')
    print("*" *(2*i-1),end='')
    print("\n")