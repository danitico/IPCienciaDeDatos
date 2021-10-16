from typing import List

def cadena_mas_larga(cadenas: List[str]) -> str:
    return max(cadenas, key=len)

lista = ['homocedasticidad', 'significativo', 'poliformismo', 'mesa']

print(f'Con la lista {lista}, la función devuelve "{cadena_mas_larga(lista)}"')
