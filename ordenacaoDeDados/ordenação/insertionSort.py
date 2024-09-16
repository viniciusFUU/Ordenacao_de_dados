lista = [3,1,5,9,8,2,4,7,6]

def insertSort(vetor):
    for i in range(1, len(vetor)):
        posicaoParaInserir = i

        valorAtual = vetor[i]
        vetor.remove(valorAtual)

        for j in range(i-1, -1, -1):
            vetorJ = vetor[j]
            if vetor[j] > valorAtual:
                posicaoParaInserir = j
        vetor.insert(posicaoParaInserir, valorAtual)

    return vetor

print(insertSort(lista))