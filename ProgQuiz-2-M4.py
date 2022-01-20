'''Write a recursive function named subsets that accepts a non-empty list of distinct integers L as argument. It should return the list of all subsets of L.
(1) Each subset is to be represented as a list of numbers.
(2) The order in which you arrange the elements within a subset doesn't matter. For L = [1, 2, 3], [1, 3] and [3, 1] represent the same subset.
(3) The order in which you append the subsets to the returned list doesn't matter.
(4) The empty list is a subset for all lists.'''

def subsets(L):
    if len(L) == 0:
        return [[]]
    S = []
    first = L[0]
    rest = L[1:]
    for sub in subsets(rest):
        S.append([first] + sub)
        S.append(sub)
    return S

print(subsets([1,2,3]))