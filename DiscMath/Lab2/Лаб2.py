A = [[0, 1, 1, 0, 0, 1, 1],  # x1
     [1, 0, 1, 0, 0, 0, 0],  # x2
     [1, 1, 0, 1, 0, 0, 0],  # x3
     [0, 0, 1, 0, 1, 1, 0],  # x4
     [0, 0, 0, 1, 0, 1, 1],  # x5
     [1, 0, 0, 1, 1, 0, 0],  # x6
     [1, 0, 0, 0, 1, 0, 1]]  # x7


def DynamicProg(matrix):

    n = len(matrix)

    start = int(input('Введите номер x начала: ')) - 1
    end = int(input('Введите номер x конца: ')) - 1

    print('Начальная Матрица Смежности:')
    print(f'    x1  x2  x3  x4  x5  x6  x7')

    for I in range(n):
        print(f'x{I + 1}', end='  ')

        for J in range(n):
            print(matrix[I][J], end='\t')
        print()
    print()

    marks = [-1] * n
    marks[start] = 0

    for i in range(n):
        av = []

        for j in range(n):
            if matrix[j][i] != 0:
                if marks[j] != -1:
                    av.append(marks[j] + matrix[j][i])

        if not av:
            continue

        min_av = min(av)
        marks[i] = min_av

    print(f"Метки всех вершин")
    print(marks)
    print(f"Кратчайший путь из x{start+1} в x{end+1}: {marks[end]}")

    return 0


def TopSort():

    n, m = [int(i) for i in input().split()]
    g = [[] for i in range(n)]
    colors = [0 for i in range(n)]
    visited = [False for i in range(n)]
    tout = []

    for i in range(m):
        a, b = [int(i) - 1 for i in input().split()]
        g[a].append(b)

    def dfs1(v):

        colors[v] = 1

        for u in g[v]:

            if colors[u] == 0:
                if dfs1(u): return True

            elif colors[u] == 1:
                return True

        colors[v] = 2

        return False

    def dfs2(v):

        visited[v] = True

        for u in g[v]:

            if not visited[u]:
                dfs2(u)

        tout.append(v)

        return False

    result = False

    for i in range(n):

        if dfs1(i):
            result = True
            break

    print(result)
    for i in range(n):
        if not visited[i]:
            dfs2(i)
    for vertex in tout[::-1]:
        print(vertex + 1)

    return 0


DynamicProg(A)

TopSort()