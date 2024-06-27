def selectionSort(vetor):
    listaOrdenada = []
    tamanhoVetor = len(vetor)

    for i in range(0, tamanhoVetor):
        menorElemento = vetor[0]

        for j in range(tamanhoVetor):
            if vetor[j] < menorElemento:
                menorElemento=vetor[j]

        listaOrdenada.append(menorElemento)
        vetor.remove(menorElemento)
        tamanhoVetor-=1

    return listaOrdenada

lista = [8, 5, 1, 3, 2, 7, 4, 9, 6, 17, 11, 19, 15]
print(selectionSort(lista))