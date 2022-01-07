import random

def Insertion_Sort(L):
    n =len(L)
    if n < 1:
        return L
    for i in range(n):
        j = i
        while(L[j] < L[j - i]):
            L[j], L[j-1] = L[j-1], L[j]
            j = j - 1
    return L


S = random.sample(range(100), 10)
print(S)
print(Insertion_Sort(S))

print(Insertion_Sort([2,5,24,796,32,35,86,21,64,8,35,46,4,13]))


def insert(L, v):
    n = len(L)
    if n == 0:
        return ([v])
    if v >= L[-1]:
        return L + [v]
    else:
        return (insert(L[:-1]), v) + L[-1:]