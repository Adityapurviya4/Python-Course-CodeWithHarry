# 2. Write a python program using function to convert Celsius to Fahrenheit.
# c =5*(f-32)/9

def fahrenheit_to_celsius(f):
    c = 5 *(f-32)/9
    return c

print(f"celsius: {fahrenheit_to_celsius(100)}")