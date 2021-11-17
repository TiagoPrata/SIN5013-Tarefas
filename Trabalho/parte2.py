# https://www.beecrowd.com.br/judge/pt/problems/view/1122

from collections import defaultdict

class URI():
    def __init__(self):
        self.positivo = [False for x in range(40)]
        self.negativo = [False for x in range(40)]
        self.T = []
        self.N = 0
        self.F = 0
        self.memo = defaultdict(dict)

    def resolvedor(self, id, soma):
        ent, saida = False, False

        if (id >= self.N and soma == self.F): return True
        elif (id >= self.N): return False
        if (soma in self.memo) & (id in self.memo[soma]): return self.memo[soma][id]

        ent = self.resolvedor(id+1, soma + self.T[id])
        saida = self.resolvedor(id+1, soma - self.T[id])

        if(ent and not saida): self.positivo[id] = True
        elif (not ent and saida): self.negativo[id] = True
        elif (ent and saida):
            self.positivo[id] = True
            self.negativo[id] = True
        self.memo[soma][id] = ent or saida

        return ent or saida


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

        valido = uri.resolvedor(0,0)
        if valido:
            for i in range(uri.N):
                if (uri.positivo[i] and uri.negativo[i]): print('?', end='')
                elif (uri.positivo[i]): print('+', end='')
                else: print('-', end='')
        else:
            print('*', end='')
        print('')