class Pilha_estatica:
    lista = []
    contador = 0

    def adicionar(elemento):
        Pilha_estatica.lista.append(elemento)

        Pilha_estatica.contador+=1

    def adicionarPelaPosicao(elemento, posicao):
        lista = Pilha_estatica.lista
        
        lista.insert(posicao, elemento)

    def removerStr(elemento):
        lista = Pilha_estatica.lista

        for obj in lista:
            if elemento == obj:
                lista.remove(elemento)
                Pilha_estatica.contador-=1

        Pilha_estatica.lista = lista

    def removerPelaPosicao(posicao):
        lista = Pilha_estatica.lista

        for i in range(len(lista)):
            if posicao == i:
                lista.remove(lista[i])

        Pilha_estatica.lista = lista

    def alterarStr(elemento, substituto):
        lista = Pilha_estatica.lista
        
        for i in range(len(lista)):
            if lista[i] == elemento:
                lista[i] = substituto

        Pilha_estatica.lista = lista

    def alterarPelaPosicao(posicao, substituto):
        lista = Pilha_estatica.lista

        for i in range(len(lista)):
            if posicao == i:
                lista[i] = substituto

        Pilha_estatica.lista = lista

    def getPosicaoElemento(elemento):
        lista = Pilha_estatica.lista

        for i in range(len(lista)):
            if elemento == lista[i]:
                return i

    def getElementoPelaPosicao(posicao):
        lista = Pilha_estatica.lista

        for i in range(len(lista)):
            if posicao == i:
                return lista[i]

    def getContador():
        return Pilha_estatica.contador
    
    def getLista():
        return Pilha_estatica.lista