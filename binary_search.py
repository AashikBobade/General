import random

def bin_search(l,x):
    '''This functin takes a sorted list, and a number say x, as two arguments'''
    if (len(l)==1):
        return (l[0]==x)

    m = len(l)//2
    if l[m]>x:
        return bin_search(l[:m],x)
    if l[m]<x:
        return bin_search(l[m:],x)
    if l[m]==x:
        return True

S = random.sample(range(30), 10) #Creates a list of 10 elements of numbers between 0 to 30 at random.
S.sort()
print(S)
print(bin_search(S,25)) #To check whether number 25 is present in our random number list passed as an argument, it may return true or may return false.
print(bin_search([1,2,3,4,5,6,7,8,9],2)) #To check whether number 2 is present in our list (2 is indeed present in our list, so this check should return true) 
