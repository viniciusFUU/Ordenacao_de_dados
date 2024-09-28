import random

def shellSort(vetor):
    tamanho_vetor = len(vetor)-1
    lista_gap = []
    gap = tamanho_vetor // 2

    while gap > 0:
        lista_gap.append(gap)
        gap = gap // 2

    for g in lista_gap:
        iteracao = 0
        while iteracao+g <= tamanho_vetor:
            if vetor[iteracao] > vetor[iteracao+g] and g > 1:
                vetor[iteracao], vetor[iteracao+g] = vetor[iteracao+g], vetor[iteracao]
            
            if g == 1:
                for i in range(1, tamanho_vetor +1):
                    elemento_x = vetor[i]

                    j = i -1
                    while j >= 0 and vetor[j] > elemento_x:
                        vetor[j+1] = vetor[j]
                        j-=1
                            
                    vetor[j+1] = elemento_x
                
                break

            iteracao+=1
    
    return vetor
            
lista = list(range(100000))
random.shuffle(lista)
print(shellSort(lista))
