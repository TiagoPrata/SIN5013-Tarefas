# https://www.beecrowd.com.br/judge/pt/problems/view/2446
# Não aceito --> Time limit exceeded

import sys

def ValOt(n, vf, va, m):
    if (n < 0) or (vf-va < 0):
        return 'N'
    if vf == va:
        return 'S'

    naousa = ValOt(n-1, vf, va, m)
    if naousa == 'S':
        return 'S'

    usa = ValOt(n-1, vf, va + m[n-1], m)
    if usa == 'S':
        return 'S'
    
    return 'N'

sys.setrecursionlimit(1500)

lin1 = list(map(int, input().split()))
moedas = list(map(int, input().split()))

valor_final = lin1[0]
num_moedas = lin1[1]

print(ValOt(num_moedas, valor_final, 0, moedas))