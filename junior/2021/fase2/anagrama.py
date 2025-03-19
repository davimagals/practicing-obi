# DESAFIO: Anagrama
# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f2/anagrama/

n = int(input())
p = input()
s = input()

lista = {}

for i in range(n):
    # primeira: soma
    caractere = p[i]

    if caractere.isalpha():
        if caractere in lista:
            lista[caractere] += 1
        else:
            lista[caractere] = 1
    
    # segunda: subtrai
    caractere = s[i]

    if caractere.isalpha():
        if caractere in lista:
            lista[caractere] -= 1
        else:
            lista[caractere] = -1


# verificar se todos zerados
for c in lista:
    if lista[c] != 0:
        print('N')
        exit()

print('S')