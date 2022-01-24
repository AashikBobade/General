n = int(input())

num = n
found = False
while not found:
    found = True
    for i in range(1, n+1):
        if num % i != 0:
            found = False
            num = num + 1
            break
print(num)