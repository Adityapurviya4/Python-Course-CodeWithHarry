# 9. Write a program to find out whether a file is identical and matches the content of another file

with open("file1.txt","r") as f:
   contain1 = f.read()

with open("file2.txt", "w") as f:
    contain2 = f.write()

if(contain1 == contain2):
    print("both file identical ")
else:
    print("No file identical ")