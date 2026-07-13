# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sumnumber(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sumnumber(3))