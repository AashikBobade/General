import random
# Selection sort is an order n ** 2 algorithm

def selection_sort(L):
    n = len(L)
    if n < 1:
        return L
    for i in range(n):
        # Assume L[:1] is sorted
        mpos = i
        # mpos: position of minimum in L[i:]
        for j in range(i+1, n):
            if L[j] < L[mpos]:
                mpos = j
        # L[mpos] : is smallest value in L[i:]
        # Exchange L[mpos] and L[i]
        L[i], L[mpos] = L[mpos], L[i]
        # Now L[:i+1] is sorted 
    return L

S = random.sample(range(100), 10)
print(S)
print(selection_sort(S)) #Code verified on a list of ten random numbers between 0 to 100
print(selection_sort([2,5,24,796,32,35,86,21,64,8,35,46,4,13])) #Code verified on a perticular list

