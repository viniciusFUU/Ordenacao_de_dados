from Filas import Filas

print(Filas.elementos)
print(Filas.isEmpty())
print(Filas.size())

Filas.enqueue(1)
Filas.enqueue(2)
Filas.enqueue(3)
Filas.enqueue(4)
print(Filas.elementos)

Filas.dequeue()
print(Filas.elementos)

print(Filas.peek())
print(Filas.isEmpty())
print(Filas.size())