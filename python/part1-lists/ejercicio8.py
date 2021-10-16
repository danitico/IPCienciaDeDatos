from typing import List

def eliminar(lista1: List[int], lista2: List[int]) -> List[int]:
    for item in lista2:
        while True:
            try:
                lista1.remove(item)
            except ValueError:
                break

    return lista1

lista1 = [1, 2, 4, 6, 7, 8]
lista2 = [1, 2, 3, 8]

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')

new_list = eliminar(lista1.copy(), lista2.copy())

print(f'La función devuelve la siguiente lista: {new_list}')
