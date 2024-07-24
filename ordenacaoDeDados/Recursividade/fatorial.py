def fatorial(qtd_numeros):
    if qtd_numeros < 1:
        return 1
    
    return qtd_numeros * fatorial(qtd_numeros-1)

print(fatorial(5))