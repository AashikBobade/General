import random  
def createList():
    '''
    this function will create a list of random numbers 
    return: An unsorted list with 10 random numbers between 0-100
    '''
    lst = random.sample(range(100), 10)
    return lst
 
def kth_largest(lst, k):
    '''
    This function will return the kth largest element present in the list
    input: An unsorted List
    return: Index that is K
    '''
    # base case
    if len(lst) < k:
        return -1
    #making copy of list
    copy_list = lst.copy()
    counter = 0
    # Finding kth Largest element
    while(len(copy_list) > 0):
        left = [] #left wing
        right = [] #right wing
        random_pivot = copy_list[0]
 
        # appending left and right wing
        for element in copy_list:
            counter+=1
            if element > random_pivot:
                right.append(element)
            if element < random_pivot:
                left.append(element)
        # checking for kth element 
        if len(left) == k-1:
            return random_pivot
        # checking if kth element is in right wing
        elif len(left) < k:
            copy_list = right
            # if left elements are chopped of K will change
            subtract_index = len(left) + 1 
            #updating K
            k = k - subtract_index 
        # if kth element is in left wing
        else:
            copy_list = left
    print(counter)
    return -1
lst = createList()
k = 6
kth_element = kth_largest(lst, k)
if(kth_element == -1):
    print("No such element exist")
else:
    lst.sort()
    print(lst)
    print("kth lasrgest is ",kth_element)