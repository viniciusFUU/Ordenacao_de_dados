def shellSort(vetor):
    tamanho_vetor = len(vetor)-1
    lista_gap = []

    for x in range(tamanho_vetor):
        for i in range(tamanho_vetor):
            gap = tamanho_vetor // 2
            
            while(gap > 0):
                if i+gap <= tamanho_vetor and vetor[i] > vetor[i+gap]:
                    vetor[i], vetor[i+gap] = vetor[i+gap], vetor[i]

                gap = gap // 2
        
    return vetor

lista = [51, 46, 73, 90, 66, 38, 13, 22, 87]
print(shellSort(lista))