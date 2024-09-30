def merge_sort(vetor):
    tamanho_vetor = len(vetor)

    if tamanho_vetor <= 1:
        return vetor

    meio = tamanho_vetor // 2

    lula = vetor[:meio]
    bolsonaro = vetor[meio:]

    esquerda = merge_sort(lula)
    direita = merge_sort(bolsonaro)

    return ordenacao(esquerda, direita)

def ordenacao(esquerda, direita):
    lista_ordenada = []
    tamanho_esq = len(esquerda)
    tamanho_dir = len(direita)

    i = 0
    j = 0

    while i < tamanho_esq and j < tamanho_dir:
        if esquerda[i] < direita[j]:
            lista_ordenada.append(esquerda[i])
            i+=1
        else:
            lista_ordenada.append(direita[j])
            j+=1

    lista_ordenada.extend(esquerda[i:])
    lista_ordenada.extend(direita[j:])

    return lista_ordenada

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(merge_sort(lista))