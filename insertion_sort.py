import random
# Insertion sort is an order n ** 2 algorithm

def Insertion_Sort(L):
    n = len(L)
    if n < 1:
        return L
    for i in range(n): #Assuming L[:i] is sorted
        j = i
        while(j > 0 and L[j] < L[j - 1]):
            L[j], L[j-1] = L[j-1], L[j] #Moving L[i] to correct position in L
            j = j - 1 #Now L[:i+1] is sorted
    return L

S = random.sample(range(100), 10)
print(S)
print(Insertion_Sort(S)) #Code verified on a list of ten random numbers between 0 to 100
print(Insertion_Sort([2,5,24,796,32,35,86,21,64,8,35,46,4,13])) #Code verified on a perticular list
