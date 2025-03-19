# DESAFIO: Pesquisa de Preços
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f2/pesquisa/

n = int(input())

compensa_lista = []

for i in range(n):
    e, a, g = input().split()
    a = float(a)
    g = float(g)

    if a <= (0.7 * g):
        compensa_lista.append(e)


if not compensa_lista:
    print('*')
else:
    for e in compensa_lista:
        print(e)