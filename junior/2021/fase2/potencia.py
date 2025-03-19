# DESAFIO: Potência
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f2/potencia/

n = int(input())

acumulado = 0

for i in range(n):
    v = input()
    p = int(v[-1])
    v = int(v[0:-1])

    acumulado += v ** p

print(acumulado)