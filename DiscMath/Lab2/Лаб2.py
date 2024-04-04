A = [[0, 1, 1, 0, 0, 1, 1],  # x1
     [1, 0, 1, 0, 0, 0, 0],  # x2
     [1, 1, 0, 1, 0, 0, 0],  # x3
     [0, 0, 1, 0, 1, 1, 0],  # x4
     [0, 0, 0, 1, 0, 1, 1],  # x5
     [1, 0, 0, 1, 1, 0, 0],  # x6
     [1, 0, 0, 0, 1, 0, 1]]  # x7


def DynamicProg(matrix):

    n = len(matrix)

    start = int(input('Введите номер x начала: ')) - 1 #Начала пути
    end = int(input('Введите номер x конца: ')) - 1 #Конец пути

    print('\nНачальная матрица смежности для метода динамического программирования:') #Вывод матрицы
    print(f'    x1  x2  x3  x4  x5  x6  x7')

    for I in range(n):
        print(f'x{I + 1}', end='  ')

        for J in range(n):
            print(matrix[I][J], end='\t')
        print()
    print()

    marks = [-1] * n #Отметки для вершин
    marks[start] = 0 #Индекс начала

    for i in range(n): #Цикл поиска отметок
        av = [] #Массив для отметок

        for j in range(n):
            if matrix[j][i] != 0:
                if marks[j] != -1:
                    av.append(marks[j] + matrix[j][i])

        if not av:
            continue

        min_av = min(av) #Минимальный путь из всех ометок на данной итерации
        marks[i] = min_av #Добавление отметки в итоговый массив пути
    #Вывод ответа
    print(f"Метки всех вершин")
    print(marks)
    print(f"Кратчайший путь из x{start+1} в x{end+1}: {marks[end]}")
    print()

    return 0


def TopSort():
    #Ввод начальной матрицы    
    matrix = [[0, 1, 0, 1, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1],
              [0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0]]
    #Вывод начальной матрицы
    print('\nМатрица смежности для топологической сортировки:')
    print(f'    x1  x2  x3  x4  x5')

    for I in range(len(matrix)):
        print(f'x{I + 1}', end='  ')

        for J in range(len(matrix)):
            print(A[I][J], end='\t')
        print()
    #Форматирование данных под алгоритм и создание массивов с отметками посещения вершин
    n, m = 5, 6
    g = [[] for i in range(n)]
    colors = [0 for i in range(n)]
    visited = [False for i in range(n)]
    tout = []

    g = [[1, 3], [2], [4], [2, 4], []]
    #Проверка на присутствие цикла в графе
    def dfs1(v):

        colors[v] = 1

        for u in g[v]:

            if colors[u] == 0:
                if dfs1(u): return True

            elif colors[u] == 1:
                return True

        colors[v] = 2

        return False
    #Основной цикл сортировки
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

    print('\nЕсть ли в графе цикл:',result)

    for i in range(n):
        if not visited[i]:
            dfs2(i)

    print('Решение:\n')

    for vertex in tout[::-1]:
        print(vertex + 1)

    return 0


DynamicProg(A)

TopSort()
