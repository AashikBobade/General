import random
#Merge sort takes time of Order n log n; O(n logn)

def merge(A,B):
    (m,n) = (len(A),len(B))
    (C,i,j,k) = ([],0,0,0)
    while k < m+n:
        if i == m:
            C.extend(B[j:])
            k = k + (n-j)
        elif j == n:
            C.extend(A[i:])
            k = k + (n-i)
        elif A[i] < B[j]:
            C.append(A[i])
            (i,k) = (i+1, k+1)
        else:
            C.append(B[j])
            (j,k) = (j+1, k+1)
    return C

def mergesort(A):
    n = len(A)

    if n <= 1:
        return A
    L = mergesort(A[:n//2])
    R = mergesort(A[n//2:])

    B = merge(L,R)

    return B

S = random.sample(range(100), 10)
print(S)
print(mergesort(S)) #Code verified on a list of ten random numbers between 0 to 100
print(mergesort([2,5,24,796,32,35,86,21,64,8,35,46,4,13])) #Code verified on a perticular list