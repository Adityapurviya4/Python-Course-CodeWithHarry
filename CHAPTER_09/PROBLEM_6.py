# 6. Write a program to mine a log file and find out whether it contains ‘pythonʼ.

word="python"
with ("log.txt", "r") as f:
    contain = f.read()

if(word in contain):
    print("yes in file word contain python")
else:
    print("no contain python")