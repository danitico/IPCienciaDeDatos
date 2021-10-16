from collections import Counter
from typing import List, Tuple

def contar_letras(palabra: str) -> List[Tuple[str, int]]:
    counter = Counter(palabra)

    return counter.most_common()

print(contar_letras('patata'))
