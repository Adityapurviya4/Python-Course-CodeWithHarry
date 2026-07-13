# 6. Write a program to calculate the factorial of a given number using for loop.

number = int(input("enter you number factorial "))

f=1
for i in range(1,number+1):
    f *=i

print(f)