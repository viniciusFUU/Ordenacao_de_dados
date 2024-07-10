def mergeSort(vetor):
    if len(vetor) <= 1:
        print(vetor)
        return vetor
    
    meio = len(vetor)//2

    esquerda = vetor[:meio]
    direita = vetor[meio:]

    ordemEsquerda = mergeSort(esquerda)
    ordemDireita = mergeSort(direita)   

lista = [5, 4, 7, 9, 6, 3, 1, 2, 8]
print(mergeSort(lista))