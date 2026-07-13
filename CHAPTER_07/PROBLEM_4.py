# 4. Write a program to find whether a given number is prime or not.

number = int(input("enter your number natural numbers : "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")
else:
    print("it is not a prime number")