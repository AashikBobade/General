'''A number is called a double palindrome if both the number and its square are palindromes. 
For example, 11 is double palindrome as both 11 and 121 are palindromes. 
Accept a positive integer n as input and print all the double palindromes less than or equal to n in ascending order.'''


def is_pal(n):
    # n = str(n)
    # return n == n[::-1]
    x = n
    x1, x2 = 0, 0
    
    while x != 0:
        x1 = x % 10
        x = x // 10
        x2 = x2 * 10 + x1
    return n == x2

n = int(input())

for i in range(1, n+1):
    if is_pal(i) and is_pal(i**2):
        print(i)
