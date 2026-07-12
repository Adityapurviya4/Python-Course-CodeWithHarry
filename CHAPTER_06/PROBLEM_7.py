# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("enter a post talking about a topic: ")

if("harry" in post.lower()):
    print("this is a post about harry")
else:
    print("this is not a post about harry")