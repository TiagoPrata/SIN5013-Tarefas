# https://www.beecrowd.com.br/judge/pt/problems/view/1122

from collections import defaultdict

class URI():
    def __init__(self):
        self.positivo = [False for x in range(40)]                                          # O(1)
        self.negativo = [False for x in range(40)]                                          # O(1)
        self.T = []                                                                         # O(1)
        self.N = 0                                                                          # Θ(1)
        self.F = 0                                                                          # Θ(1)
        self.memo = defaultdict(dict)                                                       # O(1)

    def resolvedor(self, id, soma):
        '''
        id:     indice da altura da árvore atual.
        soma:   soma acumulada dos níveis anteriores

        Esta função verifica se uma alguma folha
        da árvore apresenta uma soma igual a self.F.
        Recursivamente verifica-se os níveis mais baixos da
        árvore e assim que uma soma desejada é encontrada o
        caminho até chegar a esta folha é identificado pelos
        arrays 'positivo' e 'negativo', sendo que 'positivo[id]'
        recebe True sempre que o caminho for positivo e o mesmo
        ocorre com o array 'negativo[id]'
        '''
        ent, saida = False, False                                                           # O(1)

        if (id < 0 and soma == self.F): return True                                         # O(1)
        elif (id < 0): return False                                                         # O(1)
        if (id in self.memo) & (soma in self.memo[id]): return self.memo[id][soma]          # O(1)

        ent = self.resolvedor(id-1, soma + self.T[id])                                      # T(n-1)
        saida = self.resolvedor(id-1, soma - self.T[id])                                    # T(n-1)

        if(ent and not saida): self.positivo[id] = True                                     # O(1)
        elif (not ent and saida): self.negativo[id] = True                                  # O(1)
        elif (ent and saida):                                                               # Θ(1)
            self.positivo[id] = True                                                        # Θ(1)
            self.negativo[id] = True                                                        # Θ(1)
        self.memo[id][soma] = ent or saida                                                  # O(1)

        return (ent or saida)                                                               # Θ(1)

        '''
        Análise do algorítmo:
        Caso base:
        n = 0
            T(n) = 1                        # na verdade O(1)
            
        n > 0
            T(n) = 2T(n-1)+O(1)

            Por iteração, temos:

            it | 
            ---|---------------------------
            1  | 2T(n-1) + 1
            2  | 2[T(n-1-1)+1]+1 = 4T(n-2)+2
            3  | 2[T(n-2-1)+2]+1 = 8T(n-3)+3
            .. | ...
            i  | 2^i T(n-i) + i

            Como n-1=0 quando i=n, temos:

            T(n) = 2^n T(n-n) + n
            T(n) = 2^n T(1) + 1

            ------------------
            | T(n) = 2^n + n |
            ------------------

        Ou seja,
        NO PIOR CASO, T(n) = 2^n + c.n

        Porém,
        Como as sub-árvores são armazenadas em um variável, NO MELHOR CASO
        pode acontecer de nenhuma recursividade ser necessária, sendo assim,
        no MELHOR CASO, teríamos:

        Para n > 0:
            T(n) = T(n-1) + 1

            Por iteração, temos:

            it |
            ---|---------------------------
            1  | T(n-1) + 1
            2  | T(n-1-1)+1+1 = T(n-2) + 2
            .. | ...
            i  | T(n-i) + i

            Como n-1=0 quando i=n, temos:

            T(n) = T(n-n) + n
            T(n) = T(1) + n

            ----------------
            | T(n) = 1 + n |
            ----------------

        Ou seja,
        NO MELHOR CASO, T(n) = c.n


        Conclusão:
        ==========
            Esta função pode, no melhor caso, ter uma complexidade linear O(n) e no pior caso O(2^n + n)
        '''


if __name__=='__main__':
    while (True):
        uri = URI()
        uri.N, uri.F = list(map(int, input().split()))

        if uri.N == 0: break
        
        uri.positivo = [False for x in range(40)]
        uri.negativo = [False for x in range(40)]
        uri.T = []
        for _ in range(0,uri.N):
            uri.T = uri.T + [int(input())]

        valido = uri.resolvedor(uri.N-1,0)
        if valido:
            for i in range(uri.N):
                if (uri.positivo[i] and uri.negativo[i]): print('?', end='')
                elif (uri.positivo[i]): print('+', end='')
                else: print('-', end='')
        else:
            print('*', end='')
        print('')