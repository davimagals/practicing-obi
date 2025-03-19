# DESAFIO: Robô
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f2/robo/

n, c, s = input().split()
n = int(n)
c = int(c)
s = int(s)
comandos = input().split()

atual = 1
quant = 0

if atual == s:
    quant += 1

for i in range(c):
    d = int(comandos[i])

    if d == 1 and atual == n:
        atual = 1
    elif d == -1 and atual == 1:
        atual = n
    else:
        atual += d

    if atual == s:
        quant += 1

print(quant)