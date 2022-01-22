'''This problem is about reversing a square matrix along row or column.
The first line of the input will be an integer n, which denotes the dimension of the square matrix. 
Each of the next n lines in the input will have a sequence of n comma-separated integers. 
The last line in the input will be one of these two words: row or column. 
If it is row, then reverse the matrix along the row, else, reverse it along the column.
Print the reversed matrix as output: each line should contain one row of the matrix as a sequence of comma-separated integers.'''


def accept_mat(n):
    M = []
    
    for i in range(n):
        row = input().split(',')
        M.append([])
        for x in row:
            M[-1].append(int(x))
    return M

def reverse_row(M):
    P = []
    for row in M:
        P = [row] + P
    return P

def reverse_col(M):
    P = []
    for row in M:
        L = []
        for elem in row:
            L = [elem] + L
        P.append(L)
    return P

n = int(input())
M = accept_mat(n)

axis = input()
if axis == 'row':
    out = reverse_row(M)
else:
    out = reverse_col(M)

for i in range(n):
    for j in range(n):
        if j != n-1:
            print(out[i][j], end = ',')
        else:
            print(out[i][j])
