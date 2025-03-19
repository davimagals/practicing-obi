# DESAFIO: Plano de Internet
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f1/plano/

plano = int(input())
n = int(input())

acumulado = plano

for i in range(n):
    consumo = int(input())

    acumulado -= consumo
    acumulado += plano

print(acumulado)
