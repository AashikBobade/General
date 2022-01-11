def zero_mat(n):
    '''This function generates a nXn matrix of values as zero'''
    M = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        M.append(row)
    return M

def mat_mul(A, B):
    '''This function multiplies matrix A and matrix B'''
    n = len(A)
    prod = zero_mat(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                prod[i][j] += A[i][k] * B[k][j]
    return prod

def power(A, m):
    '''This function raises matrix A to the power m'''
    if m == 1:
        return A
    A_minus_one_power = power(A, m-1)
    return mat_mul(A_minus_one_power, A)
    
print(power([[1,1],[1,0]], 30))