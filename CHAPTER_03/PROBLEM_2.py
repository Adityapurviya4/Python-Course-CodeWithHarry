# Write a program to fill in a letter template given below with name and date

name = input("Enter your name: ")
date = input("Enter the date: ")

letter = f'''Dear {name},
You are selected!
Date: {date}
'''

print(letter)