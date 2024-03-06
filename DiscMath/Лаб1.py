import numpy as np

n = 7
m = 10

A = [[0, 1, 1, 0, 0, 1, 1],  # x1
     [1, 0, 1, 0, 0, 0, 0],  # x2
     [1, 1, 0, 1, 0, 0, 0],  # x3
     [0, 0, 1, 0, 1, 1, 0],  # x4
     [0, 0, 0, 1, 0, 1, 1],  # x5
     [1, 0, 0, 1, 1, 0, 0],  # x6
     [1, 0, 0, 0, 1, 0, 0]]  # x7

def adj_to_inc(adj_matrix):

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


def inc_to_adj(inc_matrix):
    n = len(inc_matrix)
    m = len(inc_matrix[0])

    adj_matrix = [[0] * n for _ in range(n)]

    for edge in range(m):
        for vertex in range(n):
            if inc_matrix[vertex][edge] == 1:
                for vertex2 in range(n):
                    if inc_matrix[vertex2][edge] == 1 and vertex != vertex2:
                        adj_matrix[vertex][vertex2] = 1
                        adj_matrix[vertex2][vertex] = 1
                        break

    return adj_matrix


print('Начальная Матрица Смежности:')
print(f'    x1  x2  x3  x4  x5  x6  x7')

for I in range(n):
    print(f'x{I + 1}', end='  ')

    for J in range(n):
        print(A[I][J], end='\t')
    print()
print()

Inc = adj_to_inc(A)

print('Матрица Инцидентности:')
print(f'    a1  a2  a3  a4  a5  a6  a7  a8  a9  a10')

for I in range(n):
    print(f'x{I + 1}', end='  ')

    for J in range(m):
        print(Inc[I][J], end='\t')
    print()
print()

Adj = inc_to_adj(Inc)

print('Посчитанная Матрица Смежности:')
print(f'    x1  x2  x3  x4  x5  x6  x7')

for I in range(n):
    print(f'x{I + 1}', end='  ')

    for J in range(n):
        print(Adj[I][J], end='\t')
    print()
print()
