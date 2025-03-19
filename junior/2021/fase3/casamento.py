# DESAFIO: Casamento de Inteiros
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f3/casamento/

a = input()
b = input()

if len(a) > len(b):
    dif = len(a) - len(b)
    completar = '0' * dif
    b = completar + b
elif len(b) > len(a):
    dif = len(b) - len(a)
    completar = '0' * dif
    a = completar + a


na = ''
nb = ''

for i in range(len(a)):
    if int(a[i]) >= int(b[i]):
        na += a[i]
    
    if int(b[i]) >= int(a[i]):
        nb += b[i]

na = int('-1' if na == '' else na)
nb = int('-1' if nb == '' else nb)

if na < nb:
    print(na, nb)
else:
    print(nb, na)