lista = [3,1,5,9,8,2,4,7,6]

def insertSort(vetor):
    tamanho_vetor = len(vetor)
    for i in range(1, tamanho_vetor):
        posicao_inserir = i
        valor_atual = vetor[i]
        vetor.remove(valor_atual)

        for j in range(i - 1, -1, -1):
            if valor_atual < vetor[j]:
                posicao_inserir = j

        vetor.insert(posicao_inserir, valor_atual)

    return vetor

print(insertSort(lista))