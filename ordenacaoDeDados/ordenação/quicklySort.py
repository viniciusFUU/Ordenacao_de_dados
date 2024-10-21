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
    
    vetor[fim], vetor[nao_troca+1] = vetor[nao_troca+1], vetor[fim]

    return nao_troca

lista = [30,17,16,15,29,28,27,3,2,1,22,21,26,25,24,23,10,9,8,7,6,5,4,20,19,18,14,13,12,11,]
print(quick_sort(lista, 0, len(lista) - 1))
