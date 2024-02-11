# 7x7 и 7x14
#На вход смежная

def Smejn():

    n = 7
    m = 14

    A = [[0, 1, 1, 0, 0, 0, 0],#x1
         [0, 0, 0, 1, 1, 0, 0],#x2
         [0, 1, 1, 1, 0, 1, 0],#x3
         [0, 1, 1, 0, 1, 1, 0],#x4
         [0, 0, 0, 0, 0, 1, 0],#x5
         [0, 0, 1, 0, 1, 0, 1],#x6
         [1, 0, 0, 0, 1, 0, 1]]#x7

    A = [[0, 1, 0, 0, 0, 1, 1],#x1
         [1, 0, 1, 0, 1, 0, 0],#x2
         [0, 1, 0, 1, 1, 0, 0],#x3
         [0, 0, 1, 0, 1, 0, 0],#x4
         [0, 1, 1, 1, 0, 1, 0],#x5
         [1, 0, 0, 0, 1, 0, 1],#x6
         [1, 0, 0, 0, 0, 1, 0]]#x7

    B = [[0] * 14 for I in range(7)]
    a = 0

    for i in range(0, n):
        for j in range(i, n):
            if A[i][j] == 1:
                if j == i:
                    B[i][a] = 1
                    a += 1
                elif A[j][i] == 1:
                    B[i][a] = 1
                    B[j][a] = 1
                    a += 1
                else:
                    B[i][a] = 1
                    B[j][a] = -1
                    a += 1
            else:
                if A[j][i] == 1:
                    B[i][a] = 1
                    B[j][a] = 1
                    a += 1


    print('Матрица Смежности')
    print(f'    x1  x2  x3  x4  x5  x6  x7')
    for I in range(n):
        print(f'x{I + 1}', end='  ')
        for J in range(n):
            print(A[I][J], end='\t')
        print()
    print()
    print('Матрица Инцидентности')
    print(f'    a1  a2  a3  a4  a5  a6  a7  a8  a9  a10 a11 a12 a13 a14')
    for I in range(n):
        print(f'x{I + 1}', end='  ')
        for J in range(m):
            print(B[I][J], end='\t')
        print()

Smejn()