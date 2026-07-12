# 1. Write a program to find the greatest of four numbers entered by the user.

number1 = int(input("enter the first number :"))
number2 = int(input("enter the second number :"))
number3 = int(input("enter the third number :"))
number4 = int(input("enter the fourth number :"))
                            
if(number1>number2 and number1>number3 and number1>number4):
    print("the first number is greater than all numbers")
elif(number2>number1 and number2>number3 and number2>number4):
    print("enter second number is greater than all numbers")
elif(number3>number1 and number3>number2 and number3>number4):
    print("enter third number is greater than all numbers")
else:
    print("enter fourth number is greater than all numbers")