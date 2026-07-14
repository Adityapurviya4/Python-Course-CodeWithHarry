# 4. A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

word = "Donkey"

with open("/workspaces/Python-Course-CodeWithHarry/CHAPTER_09/Donkey.txt", "r") as f:
   contnt = f.read()

contntn = contnt.replace(word,"######")

with open("/workspaces/Python-Course-CodeWithHarry/CHAPTER_09/Donkey.txt", "w") as f:
            f.write(contnt)