def mergeSort(vetor):
    if len(vetor) <=1:
        return vetor
    
    meio = len(vetor)//2

    esquerda = vetor[:meio]
    direita = vetor[meio:]

    lula = mergeSort(esquerda)
    bolsonaro = mergeSort(direita)

    return ordenacao(lula, bolsonaro)

def ordenacao(esquerda, direita):
    lulonaro = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lulonaro.append(esquerda[i])
            i+=1
        else:
            lulonaro.append(direita[j])
            j+=1

    lulonaro.extend(esquerda[i:])
    lulonaro.extend(direita[j:])

    return lulonaro

lista = [3, 7, 6, -10, 15, 23.5, 55, -13]
print(mergeSort(lista))