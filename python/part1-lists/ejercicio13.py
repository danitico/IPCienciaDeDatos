from typing import List, Tuple

def dispersa(v: List[int]) -> Tuple[List[Tuple[int, int]], int]:
    non_null_values = []
    length_v = len(v)

    for index in range(length_v):
        if v[index] != 0:
            non_null_values.append((index, v[index]))

    return (non_null_values, length_v)

example = [1, 0, 0, 5, 4, 0, 0, 0]

print(f'Con la lista {example} la función devuelve {dispersa(example)}')
