import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
numeros = [random.randint(1, 100) for _ in range(10)]

ordenada = bubble_sort(numeros)

print(ordenada)
