import numpy as np
# 7x7 и 7x14
#На вход смежная

n = 7
m = 14

A = [[0, 1, 1, 0, 0, 0, 0],  # x1
     [0, 0, 0, 1, 1, 0, 0],  # x2
     [0, 1, 1, 1, 0, 1, 0],  # x3
     [0, 1, 1, 0, 1, 1, 0],  # x4
     [0, 0, 0, 0, 0, 1, 0],  # x5
     [0, 0, 1, 0, 1, 0, 1],  # x6
     [1, 0, 0, 0, 1, 0, 1]]  # x7

# A = [[0, 1, 0, 0, 0, 1, 1],  # x1
#      [1, 0, 1, 0, 1, 0, 0],  # x2
#      [0, 1, 0, 1, 1, 0, 0],  # x3
#      [0, 0, 1, 0, 1, 0, 0],  # x4
#      [0, 1, 1, 1, 0, 1, 0],  # x5
#      [1, 0, 0, 0, 1, 0, 1],  # x6
#      [1, 0, 0, 0, 0, 1, 0]]  # x7

def adj_matrix_to_inc_matrix(adj_matrix):

    n = len(adj_matrix)
    m = n * (n - 1) // 2

    inc_matrix = [[0] * m for _ in range(n)]
    edge_index = 0

    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] != 0:
                inc_matrix[i][edge_index] = 1
                inc_matrix[j][edge_index] = 1
                edge_index += 1

    return inc_matrix


print('Матрица Смежности')
print(f'    x1  x2  x3  x4  x5  x6  x7')

for I in range(n):
    print(f'x{I + 1}', end='  ')

    for J in range(n):
        print(A[I][J], end='\t')
    print()
print()

Inc = adj_matrix_to_inc_matrix(A)

print('Матрица Инцидентности')
print(f'    a1  a2  a3  a4  a5  a6  a7  a8  a9  a10 a11 a12 a13 a14')

for I in range(n):
    print(f'x{I + 1}', end='  ')

    for J in range(m):
        print(Inc[I][J], end='\t')
    print()