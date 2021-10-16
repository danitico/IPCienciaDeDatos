def anagrama(palabra1: str, palabra2: str) -> bool:
    palabra1_lista = [letter for letter in palabra1]
    palabra2_lista = [letter for letter in palabra2]

    palabra1_lista.sort()
    palabra2_lista.sort()

    return palabra1_lista == palabra2_lista

print(f'Con la palabra gato y toga la función devuelve {anagrama("gato", "toga")}')
print(f'Con la palabra gato y mesa la función devuelve {anagrama("gato", "mesa")}')
