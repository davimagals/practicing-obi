# DESAFIO: Idade de Camila
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f1/idade/

# Cibele < Camila < Celeste
#             ?

x = int(input())
y = int(input())
z = int(input())

if y <= x <= z or z <= x <= y:
    print(x)
elif x <= y <= z or z <= y <= x:
    print(y)
else:
    print(z)