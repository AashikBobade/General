import sys
sys.setrecursionlimit(2**31-1)

def factorial(n):
    fact = 1
    if (n == 0):
        return fact
    elif (n < 0):
        return 'Invalid'
    else:
        return(factorial(n-1)*n)

print(factorial(1000))