def quicklySort(vetor):
    if len(vetor) <= 1:
        return vetor
    
    pivo = vetor[0]

    menor = []
    maior = []

    for i in range(1, len(vetor)):
        if vetor[i] > pivo:
            maior.append(vetor[i])
        else:
            menor.append(vetor[i])

    menores = quicklySort(menor)
    maiores = quicklySort(maior)

    return menores + [pivo] + maiores

lista = [5, 4, 7, 9, 6, 3, 1, 2, 8]

print(quicklySort(lista))