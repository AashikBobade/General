'''Consider a sequence of words. A sub-sequence is a subset of consecutive words in this sequence. For example, given the following sequence:
   one,two,order,real,long,tight,tree,cool,lot,trouble 
   
   The following are some sub-sequences:
    (1) one,two,order
    (2) real,long,tight,tree
    (3) cool
    (4) one,two,order,real,long,tight,tree,cool,lot,trouble

    Note that one,lot does not form a sub-sequence as far as this problem is concerned. (3) and (4) are valid sub-sequences even though they are quite trivial in nature.
    A sub-sequence is said to have the antakshari property if the last letter of every word in the sub-sequence is equal to the first letter in the next word. 
    For example, in the above sequence, we have the following sub-sequences with this property:
    
    cool,lot
    cool,lot,trouble
    two,order,real
    two,order,real,long
    
    Your task is to find the length of the longest sub-sequence with the antakshari property. 
    In the above sequence, the longest sub-sequence with this property has length 4.
    
    Accept a sequence of comma separated words as input and print the length of the longest sub-sequence with the antakshari property. 
    All words in the sequence will be in lower case.'''


words = input().split(',')
n = len(words)
max_count = 1
for i in range(n):
    word = words[i]
    j, count = i + 1, 1
    while j < n:
        if words[j][0] == word[-1]:
            count += 1
            word = words[j]
            j += 1
        else:
            break
    if count > max_count:
        max_count = count
print(max_count)
