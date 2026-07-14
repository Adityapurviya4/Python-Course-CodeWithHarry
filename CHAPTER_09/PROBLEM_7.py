# 7. Write a program to find out the line number where python is present from ques 6.

with ("log.txt", "r") as f:
    line=1
    word="python"
    lines = f.readlines()
for line in lines:
    if(word in line):
       print("yes in file word contain python no: " , line)
    else:
       print("no contain python")