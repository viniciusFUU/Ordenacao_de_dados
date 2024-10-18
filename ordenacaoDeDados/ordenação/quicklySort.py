def quickly_sort(vetor):
    tamanho_lista = len(vetor)-1
    if tamanho_lista < 1:
        return vetor
    
    pivo = vetor[-1]
    vetor_param = 0
    vetor_param_novo = 0

    for i in range(tamanho_lista):

        if pivo >= vetor[i]:
            vetor_param_novo = i

        if vetor[vetor_param] > vetor[vetor_param_novo]:
            vetor[vetor_param_novo], vetor[vetor_param] = vetor[vetor_param], vetor[vetor_param_novo]
            vetor_param+=1

    if vetor[-1] < vetor[vetor_param-1]:
        vetor[-1], vetor[vetor_param-1] = vetor[vetor_param-1], vetor[-1]
    
    print("fim")
    esquerda = separando_listas(vetor, 0, vetor_param-1)
    direita = separando_listas(vetor, vetor_param, -1)

    quickly_sort(esquerda)
    quickly_sort(direita)

    return esquerda + [pivo] + direita

def separando_listas(vetor, inicio, fim):
    vetor_adaptado = vetor[inicio:fim]

    return vetor_adaptado

lista = [10, 9, 5, 1, 4, 3, 28, 7, 6]
print(quickly_sort(lista))