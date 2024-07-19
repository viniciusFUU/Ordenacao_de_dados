def listar_letras(palavra):
    palabra_inversa = palavra[-1]

    qtd_letras = len(palavra)-1

    if qtd_letras < 1:
        return palabra_inversa

    palavra = palavra[0:-1]

    return palabra_inversa + listar_letras(palavra)

print(listar_letras("abcdefg"))