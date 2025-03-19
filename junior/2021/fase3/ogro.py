# DESAFIO: Ogro
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f3/ogro/

n = int(input())

e = ''
d = ''

if n == 0:
    e = '*'
    d = '*'
elif n <= 5:
    e = n * 'I'
    d = '*'
else:
    e = 5 * 'I'
    d = (n - 5) * 'I'

print(e)
print(d)