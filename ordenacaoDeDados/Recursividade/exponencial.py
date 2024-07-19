def exponencial(numero, qtd):
    if qtd < 1:
        return 1
    
    return numero * exponencial(numero, qtd-1)

print(exponencial(10, 4))
