# 5. Repeat program 4 for a list of such words to be censored.

word = ["Donkey","bad"]

with ("Donkey.txt", "r") as f:
     context = f.read()

for word in word:
    context = context.replace(word,"#####")

with ("Donkey.txt", "w") as f:
     f.write(context)