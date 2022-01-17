import sys
sys.setrecursionlimit(2**31-1)

def factorial(n):
    '''Recursive way to find factorial of a number'''
    fact = 1
    if (n == 0):
        return fact
    elif (n < 0):
        return 'Invalid'
    else:
        return(factorial(n-1)*n)

print(factorial(5))
print(factorial(1))
print(factorial(0))
print(factorial(1000))
