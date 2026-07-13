# 6. Write a python function which converts inches to cms.

def coverts(i):
    c = i * 2.54
    return c

i = int(input("Enter your number to convert inches to centimeters: "))
print(coverts(i))