from collections import Counter
from typing import List, Tuple

def contar_letras(palabra: str) -> List[Tuple[str, int]]:
    # this does the same
    # return Counter(palabra).most_common()
    palabra = palabra.lower()
    unique_letters = set(palabra)

    return [(letter, palabra.count(letter)) for letter in unique_letters]

print(contar_letras('patata'))
