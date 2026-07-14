# 2. The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
# Hi-score. You need to write a program to update the Hi-score whenever the game()
# function breaks the Hi-score.

import random

def game():
    print("welcome to the number guessing game : ")
    number = random.randint(1,100)

    with open("/workspaces/Python-Course-CodeWithHarry/CHAPTER_09/Hi_score.txt") as f:
        hi_score = f.read()
        if(hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score =0
    
    print("The high score is : ", hi_score)
    if(number>hi_score):
        print("you have set a new high score : ",number)
        with open("/workspaces/Python-Course-CodeWithHarry/CHAPTER_09/Hi_score.txt", "w") as f:
            f.write(str(number))
            return number
        

game()