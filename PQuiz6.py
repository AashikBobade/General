'''Three rectangular matrices A, B and C are provided to you. 
    You need to compute the product of these three matrices: A X B X C. 
    Store the results of this matrix multiplication in a matrix named as prod. 
    Each of these matrices is a list of lists.'''

def multiply(A, B, C):
    temp =[]        
    for i in range(len(A)):
        temp.append([])
        for j in range(len(B[0])):
            temp[i].append(0)
            for k in range(len(B)):
                temp[i][j] += A[i][k] * B[k][j]
    prod = []
    for i in range(len(A)):
        prod.append([])
        for j in  range(len(C[0])):
            prod[i].append(0)
            for k in range(len(B[0])):
                prod[i][j] += temp[i][k] * C[k][j]
    return prod

print(multiply([[1,2],[2,3]],[[1,2],[2,3]],[[1,2],[2,3]]))
