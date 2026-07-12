# 3. A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

p1= "Make a lot of money"
p2= "buy now"
p3= "subscribe this"
p4= "click this"

message = input("enter the message : ")

if(message in p1 or message in p2 or message in p3 or message in p4):
    print("this comment are span")
else:
    print("this comment are not span")