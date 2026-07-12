# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F



grade = int(input("enter your marksa :"))

if(grade>90 or grade>=100):
    print("your grade is EX")
elif(grade>80 or grade<=90):
    print("your grade is A")
elif(grade>70 or grade <=80):
    print("your grade is B")
elif(grade>60 or grade <=70):
    print("your grade is C")
elif(grade>50 or grade <=60):
    print("your grade is D")
else:
    print("your grade is F")