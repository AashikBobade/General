''' Program to create an identity matrix of order n'''
n = int(input())
I = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    I.append(row)

'''Printing the matrix in traditional matrix format'''
for i in range(n):
    for j in range(n):
        if j != n-1:
            print(I[i][j], end = ',')
        else:
            print(I[i][j])