# DESAFIO: Pangrama
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f2/pangrama/

frase = input()

alfabeto = 'abcdefghijlmnopqrstuvxz'

for l in alfabeto:
    if l not in frase:
        print('N')
        exit()

print('S')