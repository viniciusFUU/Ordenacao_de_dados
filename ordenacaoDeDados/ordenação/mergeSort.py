def merge_sort(vetor, inicio, fim):
    meio = (inicio + fim) // 2

    if inicio >= fim:
        return
    
    merge_sort(vetor, inicio, meio)
    merge_sort(vetor, meio+1, fim)

    ordenacao(vetor, inicio, meio, fim)

    return vetor

def ordenacao(vetor, inicio, meio, fim):
    esquerda = vetor[inicio:meio+1]
    direita = vetor[meio+1:fim+1]
    tamanho_esquerda = len(esquerda)
    tamanho_direita = len(direita)

    posicao = inicio
    i = j = 0

    while i < tamanho_esquerda and j < tamanho_direita:
        if esquerda[i] > direita[j]:
            vetor[posicao] = direita[j]
            j+=1
        else:
            vetor[posicao] = esquerda[i]
            i+=1
        posicao+=1
    
    while i < tamanho_esquerda:
        vetor[posicao] = esquerda[i]
        i+=1
        posicao+=1

    while j < tamanho_direita:
        vetor[posicao] = direita[j]
        j+=1
        posicao+=1

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
inicio = 0
fim = len(lista)-1
print(merge_sort(lista, inicio, fim))