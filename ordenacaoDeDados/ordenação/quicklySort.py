def quickly_sort(vetor):
    tamanho_vetor = len(vetor)

    if tamanho_vetor < 1:
        return vetor
    
    pivo = vetor[0]

    menor = []
    maior = []

    for i in range(1, tamanho_vetor):
        if vetor[i] > pivo:
            maior.append(vetor[i])
        else:
            menor.append(vetor[i])

    esquerda = quickly_sort(menor)
    direita = quickly_sort(maior)

    return esquerda + [pivo] + direita

lista = [10, 9, 5, 1, 4, 3, 28, 7, 6]

print(quickly_sort(lista))