def fibonacci(qtd_numeros):
    if qtd_numeros < 1:
        return 0
    elif qtd_numeros == 1:
        return 1
    else:
        return fibonacci(qtd_numeros-1) + fibonacci(qtd_numeros-2)
    
print(fibonacci(5))

#0, 1, 1, 2, 3, 5