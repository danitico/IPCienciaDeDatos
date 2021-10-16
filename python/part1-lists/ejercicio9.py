from typing import List

def suma_acumulada(numeros: List[int]) -> int:
    return [
        sum(numeros[:(index + 1)])
        for index in range(len(numeros))
    ]

lista = [1, 2, 3]

print(f'Con la lista {lista}, la función devuelve {suma_acumulada(lista)}')
