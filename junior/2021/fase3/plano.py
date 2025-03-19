# DESAFIO: Plano de Estacionamento

n = int(input())
m = int(input())

vi_lista = []
for i in range(m):
    vi_lista.append(int(input()))


vagas = [False] * n
atendidos_n = 0

for vi in vi_lista:
    atendidoOk = False

    for j in range(vi):
        if vagas[j] == False:
            vagas[j] = True

            atendidoOk = True
            atendidos_n += 1

            break
    
    if not atendidoOk:
        break


print(atendidos_n)