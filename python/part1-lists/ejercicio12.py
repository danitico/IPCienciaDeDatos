from typing import List

from math import log, log10

def get_first_digit(numero: int) -> int:
    return numero // (10 ** int(log10(numero)))

def suma_primer_digito(numeros: List[int]) -> int:
    return sum([
        get_first_digit(numero)
        for numero in numeros
    ])

numeros = [40, 21, 4531, 34]

print(f'Con la lista {numeros} la función devuelve {suma_primer_digito(numeros)}')
