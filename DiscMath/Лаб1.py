import numpy as np

n = 7 #Количество строк и столбцов
m = 10 #Количество столбцов в инцидентности

#Исходная матрица смежности:
A = [[0, 1, 1, 0, 0, 1, 1],  # x1
     [1, 0, 1, 0, 0, 0, 0],  # x2
     [1, 1, 0, 1, 0, 0, 0],  # x3
     [0, 0, 1, 0, 1, 1, 0],  # x4
     [0, 0, 0, 1, 0, 1, 1],  # x5
     [1, 0, 0, 1, 1, 0, 0],  # x6
     [1, 0, 0, 0, 1, 0, 1]]  # x7

def adj_to_inc(adj_matrix): #Смежность в инцидентность

    n = len(adj_matrix) #Размер матрицы
    m = 10 #Количество столбцов в матрице инцидентности

    inc_matrix = [[0] * m for _ in range(n)] #Создание пустой матрицы инцидентности
    edge_index = 0 #Счетчик ребер

    for i in range(n): #Перебор строк
        for j in range(i + 1, n): #Перебор столбцов
            if adj_matrix[i][j] != 0: #Если элемент ij матрицы смежности не равен нулю:
                inc_matrix[i][edge_index] = -1 #Присваивание значения элементам матрицы инцидентности
                inc_matrix[j][edge_index] = 1
                edge_index += 1 #Счетчик ребер +1

    return inc_matrix


def inc_to_adj(inc_matrix): #Инцидентность в смежность
    n = len(inc_matrix)    #Колво строк матрицы инц
    m = len(inc_matrix[0]) #Колво столбцов матрицы инц

    adj_matrix = [[0] * n for _ in range(n)] #Создание пустой матрицы смежности

    for edge in range(m): #Прохождение по столбцам
        for vertex in range(n): #Прохождение по строкам
            if inc_matrix[vertex][edge] == 1: #Если элемент матрицы инцидентности = 1
                for vertex2 in range(n): #Прохождение по строкам снова
                    if (inc_matrix[vertex2][edge] == 1 and vertex != vertex2) or (inc_matrix[vertex2][edge] == - 1 and vertex != vertex2): #Если элемент матрицы инцидентности = 1 и мы не на главной диагонали:
                        adj_matrix[vertex][vertex2] = 1 #Присваиваем значения элементам матрицы смежности
                        adj_matrix[vertex2][vertex] = 1
                        break

    return adj_matrix

############################################################
#Защита исполнение

def Gx(Inc, xi):

    indexes = [i for i, v in enumerate(Inc[xi]) if v == -1]

    Gx = []

    for a in range(len(indexes)):
        for i in range(len(Inc)):
            if Inc[i][indexes[a]] == 1:
                Gx.append(i+1)

    return Gx

############################################################
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
print(f'    u1  u2  u3  u4  u5  u6  u7  u8  u9  u10')

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

#         u1  u2  u3  u4  u5  u6  u7  u8  u9  u10
Inc =  [[-1, -1, -1, -1,  0,  0,  0,  0,  0,  0],   #x1
         [1,  0,  0,  0, -1,  0,  0,  0,  0,  0],	#x2
         [0,  1,  0,  0,  1, -1,  0,  0,  0,  0],	#x3
         [0,  0,  0,  0,  0,  1, -1, -1,  0,  0],   #x4
         [0,  0,  0,  0,  0,  0,  1,  0, -1, -1],   #x5
         [0,  0,  1,  0,  0,  0,  0,  1,  1,  0],   #x6
         [0,  0,  0,  1,  0,  0,  0,  0,  0,  1]]   #x7

xi = int(input('Введите i для xi: ')) -1
gx = Gx(Inc, xi)
print(f'G-(x{xi+1})= ( ', end='')
for i in range(len(gx)):
    print(f'x{gx[i]}', end=' ')
print(')')