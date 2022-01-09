import sys
sys.setrecursionlimit(2**31-1)

import random
def create_list(n,r): #creating a list of random numbers
    L = []
    for _ in range(n):
        L.append(random.randint(1,r))
    return L

def quicksort(L, l, r): # sort L[l:r]
    if (r - l <= 1):
        return L
    (pivot, lower, upper) = (L[l], l+1, l+1)
    for i in range(l+1, r):
        if L[i] > pivot:
            upper = upper + 1
        else:
            (L[i], L[lower]) = (L[lower], L[i])
            lower, upper = lower+1, upper+1
    (L[l], L[lower-1]) = L[lower-1], L[l]
    lower = lower - 1
    quicksort(L, l, lower) #recursive call
    quicksort(L, lower+1, upper) 
    return L

L = create_list(10,100)
print(L)
print(quicksort(L,0,10))
print(quicksort([6,1,2,8,7,13,5,9,4], 0, 9))