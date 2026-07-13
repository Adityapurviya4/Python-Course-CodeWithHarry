# 1. Write a program using functions to find greatest of three numbers.

def greater(a,b,c):
    if(a>b and a>c):
        print("a is greater")
    elif(b>a and b>c):
        print("b is greater")
    else:
        print("c is greater")

greater(10,20,30)