# 7. Write a python function to remove a given word from a list and strip it at the same time.

l =["harry", "rohan", "skillf", "shubham", "mohit", "an"]

def rem(l, word):
    n=[]
    for item in l:
        if not(word == item):
            n.append(item.strip(word))
    return n

print(rem(l,"an"))