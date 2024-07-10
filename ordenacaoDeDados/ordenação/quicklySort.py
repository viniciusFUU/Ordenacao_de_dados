def quicklySort(vetor):
    pivo = vetor[0]

    for i in range(len(vetor)):
        valorAtual = vetor[i]
        
        if valorAtual < pivo:
            vetor.remove(valorAtual)
            vetor.insert(0, valorAtual)

    valorPivo = 0

    for n in range(0, pivo):
        valorPivo+=1

    valorComparado=valorPivo-2

    if valorPivo >= 0:
        for i in range(valorPivo-1, -1, -1):
            pivo=vetor[i-1]

            valorAtual = valorComparado
            
            if valorAtual < pivo:
                vetor.remove(valorAtual)
                vetor.insert(0, valorAtual)
                valorComparado-=1

    for i in range(len(vetor) - 1, valorPivo - 1, -1):
        pivo = vetor[i]

        for j in range(valorPivo, len(vetor)):
            valorAtual=vetor[j]
            if pivo > valorAtual:
                vetor.remove(valorAtual)
                vetor.insert(valorPivo, valorAtual)

            # if valorAtual < pivo:



    print(vetor)

lista = [5, 4, 7, 9, 6, 3, 1, 2, 8]
print(quicklySort(lista))