def ordenacaoAleatoria(vetor):
    valorAtual = vetor[0]
    contador = 0

    while contador < len(vetor):
        for i in range(1, len(vetor)):
            for j in range(i-1, -1, -1):
                if vetor[i] < vetor[j]:
                    valorAtual=vetor[i]
                    vetor.remove(valorAtual)    
                    vetor.insert(j, valorAtual)
        contador+=1
    
    return vetor

lista = [3,1,5,9,8,2,4,7,6]
print(ordenacaoAleatoria(lista))
