def quick_sort(vetor, inicio, fim):
    if inicio < fim:
        pivo = ordenar(vetor, inicio, fim)

        quick_sort(vetor, inicio, pivo)
        quick_sort(vetor, pivo+2, fim)
    
    return vetor

def ordenar(vetor, inicio, fim):
    pivo = vetor[fim]
    nao_troca = inicio-1
    troca = inicio

    for i in range(inicio, fim):
        if vetor[i] < pivo:
            troca = i
            nao_troca+=1
            vetor[nao_troca], vetor[troca] = vetor[troca], vetor[nao_troca]

    
    if pivo < vetor[nao_troca+1]:
        vetor[fim], vetor[nao_troca+1] = vetor[nao_troca+1], vetor[fim]

    return nao_troca

lista = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
print(quick_sort(lista, 0, len(lista) - 1))
