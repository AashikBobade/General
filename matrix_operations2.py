n = int(input())
#initialization and populating matrix A
A = []
for i in range(n):
  row = input().split(',')
  for j in range(n):
    row[j] = int(row[j])
  A.append(row)

#initialization and populating matrix B
B = []
for i in range(n):
  row = input().split(',')
  for j in range(n):
    row[j] = int(row[j])
  B.append(row)

#initialization of matrix C
C = []
for i in range(n):
  row = []
  for j in range(n):
    row.append(0)
  C.append(row)

#populating matrix C (A X B)
for i in range(n):
  for j in range(n):
    for k in range(n):
      C[i][j] = C[i][j] + A[i][k]*B[k][j]

#printing C
for i in range(n):
  for j in range(n):
    if (j != n-1):
      print(C[i][j], end = ',')
    else:
      print(C[i][j])