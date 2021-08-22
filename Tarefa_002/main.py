#################################################
## Autor: Tiago Prata
## Data: 22-Ago-2021
##
## Dado um número x e um vetor A[1... n], escreva em pseudocódigo um algoritmo
## recursivo de busca binária para encontrar j tal que A[j-1] < x ≤ A[j].
## A função deve ter os seguintes parâmetros: 
## ● Vetor A com n elementos 
## ● Inteiro e que representa a posição do lado esquerdo do vetor 
## ● Inteiro d que representa a posição do lado direito do vetor 
## ● Valor x com o elemento que se deseja encontrar
##
#################################################

def busca_binaria(A, e, d, x):
    meio = (int)((e+d)/2)
    if A[meio] == x: return meio
    if len(A[e:d+1]) == 1: return meio + 1
    if A[meio] < x:
        return busca_binaria(A, meio+1, d, x)
    else:
        return busca_binaria(A, e, meio-1, x)


if __name__ == '__main__':
    A = [10, 20, 30, 40, 50, 60]
    x = 45

    ans = busca_binaria(A, 0, len(A)-1, x)
    print(ans)