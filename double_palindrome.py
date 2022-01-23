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