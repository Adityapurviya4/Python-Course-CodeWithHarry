
# 1. Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
# contains the word ‘twinkleʼ.

f = open("/workspaces/Python-Course-CodeWithHarry/CHAPTER_09/poems.txt")

contain = f.read()
if("twinkle" in contain):
    print("YES")
else:
    print("No")
f.close()