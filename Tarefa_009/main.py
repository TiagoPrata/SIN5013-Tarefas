def PreProcessar(A, n, k):
    B = [0] * k
    for i in range(0, n):
        B[A[i]] += 1

    C = [[0 for x in range(k)] for y in range(k)] 
    for i in range(0, k-1):
        for j in range(i, k):
            if i == j:
                C[i][j] = B[i]
            else:
                C[i][j] = C[i][j-1] + B[j]

    return C

def ResponderQuery(a, b, MatrizPreProcessada):
    return MatrizPreProcessada[a][b]


if __name__=='__main__':
    A = [50, 60, 70]

    Matriz = PreProcessar(A, 3, 100)
    print(ResponderQuery(45, 65, Matriz))