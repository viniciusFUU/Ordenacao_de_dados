def selectionSort(vetor):
    posicao = 1
    menor_posicao = 0

    for i in range(len(vetor)):
        elementoX = vetor[i]

        for j in range(posicao, len(vetor)):
            if elementoX > vetor[j]:
                elementoX = vetor[j]
                menor_posicao = j

        if vetor[i] > vetor[menor_posicao]:
            vetor[i], vetor[menor_posicao] = vetor[menor_posicao], vetor[i]

        posicao+=1

    return vetor

lista = [8, 5, 1, 3, 2, 7, 4, 9, 6, 17, 11, 19, 15]
print(selectionSort(lista))