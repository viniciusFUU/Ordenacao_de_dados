# 8, 5, 1, 3, 2, 7, 4, 9, 6
# 1, 2, 3, 4, 5, 6, 7, 8, 9

def bubbleSort(vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor)-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

    return vetor

lista = [8, 5, 1, 3, 2, 7, 4, 9, 6]
print(bubbleSort(lista))