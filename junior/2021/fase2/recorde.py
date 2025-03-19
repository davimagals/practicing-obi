# DESAFIO: Recorde
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f2/recorde/

r = int(input())
m = int(input())
l = int(input())

if r < m:
    print('RM')
else:
    print('*')

if r < l:
    print('RO')
else:
    print('*')