# DESAFIO: Cifra da Nlogônia
# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/cifra/

#palavra = input()
palavra = "ter"

saida = ''

alfabeto = "abcdefghijklmnopqrstuvxz"

pos_letra = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
 'u': 20, 'v': 21, 'x': 22, 'z': 23}

for c in palavra:
    if c not in "aeiou":
        pos_c = pos_letra[c]

        pos_a = 0
        pos_p = 0
        for _ in range(6):
            