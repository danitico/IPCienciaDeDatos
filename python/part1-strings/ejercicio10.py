def es_inversa(palabra1: str, palabra2: str) -> bool:
    palabra1_list = [letter for letter in palabra1]
    palabra2_list = [letter for letter in palabra2]

    palabra2_list.reverse()

    return palabra1_list == palabra2_list

print(f'Con las palabras mesa y gato la función devuelve {es_inversa("mesa", "gato")}')
print(f'Con las palabras absd y dsba la función devuelve {es_inversa("absd", "dsba")}')
