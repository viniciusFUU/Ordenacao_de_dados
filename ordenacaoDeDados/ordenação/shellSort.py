def shellSort(vetor):
    tamanho_vetor = len(vetor)-1
    lista_gap = []
    gap = tamanho_vetor//2

    while gap > 0:
        lista_gap.append(gap)
        gap //=2


    for x in range(tamanho_vetor):
        for i in range(tamanho_vetor):                
            for g in lista_gap:        
                if i+g <= tamanho_vetor and vetor[i] > vetor[i+g]:            
                    vetor[i], vetor[i+g] = vetor[i+g], vetor[i]

    return vetor

lista = [51, 46, 73, 90, 66, 38, 13, 22, 87]
print(shellSort(lista))