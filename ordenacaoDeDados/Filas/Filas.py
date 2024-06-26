class Filas:
    elementos = []
    quantidade_elementos = 0

    def enqueue(elemento):
        lista = Filas.elementos

        lista.append(elemento)
        Filas.quantidade_elementos+=1

        Filas.elementos = lista

    def dequeue():
        lista = Filas.elementos

        lista.remove(lista[0])
        Filas.quantidade_elementos-=1

        Filas.elementos = lista

    def peek():
        if Filas.isEmpty == True:
            return "Lista vazia"
        
        return Filas.elementos[0]


    def isEmpty():
        if len(Filas.elementos) == 0:
            return True
        
        return False
    
    def size():
        return Filas.quantidade_elementos