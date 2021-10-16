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


def es_triple_doble(palabra: str) -> bool:
    if not palabra or len(palabra) < 6:
        return False

    first_list = [item for item in trocear(palabra, 2) if len(item) > 1]
    second_list = [item for item in trocear(palabra[1:], 2) if len(item) > 1]

    count_first_list = 0
    count_second_list = 0

    for item in first_list:
        if item[0] == item[1]:
            count_first_list += 1
        elif count_first_list < 3:
            count_first_list = 0

    for item in second_list:
        if item[0] == item[1]:
            count_second_list += 1
        elif count_second_list < 3:
            count_second_list = 0

    return count_first_list == 3 or count_second_list == 3

example = "abgghhkkerf"

print(f'Con la palabra "{example}" la función devuelve {es_triple_doble(example)}')
