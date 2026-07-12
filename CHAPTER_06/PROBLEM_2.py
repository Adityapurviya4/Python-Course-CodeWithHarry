# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.

Physics = int(input("enter the marks for Physics :"))
Chemistry = int(input("enter the marks for Chemistry :"))
Mathematics = int(input("enter the marks for Mathematics :"))

total_percentage = 100 * (Physics + Chemistry + Mathematics)/300

if(total_percentage>=40 and Physics>=33 and Chemistry>=33 and Mathematics>=33):
    print("passed",total_percentage)
else:
    print("failed",total_percentage)