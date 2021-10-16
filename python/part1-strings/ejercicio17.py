from typing import List

def trocear(palabra: str, num: int) -> List[str]:
    index = 0
    lista_trozeada = []

    while index < len(palabra):
        lista_trozeada.append(
            palabra[index:(index + num)]
        )
        index += num

    return lista_trozeada


print(trocear('gatogat', 2))
