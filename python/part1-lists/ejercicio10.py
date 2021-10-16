from typing import List, Tuple

def parejas(lista: List[int]) -> List[Tuple[int, int]]:
    return [(x, y) for x in lista for y in lista]

lista = [1, 2, 3]

print(f'Con la lista {lista} se devuelven las siguientes parejas {parejas(lista)}')
