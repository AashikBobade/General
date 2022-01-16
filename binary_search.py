import random

def bin_search(l,x):
    if (len(l)==1):
        return (l[0]==x)

    m = len(l)//2
    if l[m]>x:
        return bin_search(l[:m],x)
    if l[m]<x:
        return bin_search(l[m:],x)
    if l[m]==x:
        return True

S = random.sample(range(30), 10)
S.sort()
print(S)
print(bin_search(S,25))
print(bin_search([1,2,3,4,5,6,7,8,9],2))