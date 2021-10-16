from typing import List

def mezclar(lista1: List[int], lista2: List[int]) -> List[int]:
    lista = lista1 + lista2
    lista.sort()

    return lista

lista1 = [6, 7, 8]
lista2 = [1, 2, 3]

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'La función devuelve {mezclar(lista1, lista2)}')
