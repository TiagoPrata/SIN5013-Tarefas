# https://www.beecrowd.com.br/judge/en/runs/code/25141277
# Não aceito --> Time limit exceeded

lin1 = list(map(int, input().split()))
moedas = list(map(int, input().split()))

valor_final = lin1[0]
num_moedas = lin1[1]

somas_possiveis = [0 for x in range(valor_final)]
somas_possiveis[0] = 1

for i in range(num_moedas):
    for v in range(valor_final, moedas[i], -1):
        if somas_possiveis[v-moedas[i]-1]:
            somas_possiveis[v-1] = 1

if somas_possiveis[valor_final-1] ==1:
    print('S')
else:
    print('N')