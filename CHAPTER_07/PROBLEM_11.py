# 10. Write a program to print multiplication table of n using for loops in reversed order.

number = int(input("enter your number to table : "))

for i in range(1,11):
    print(number * (11-i))
