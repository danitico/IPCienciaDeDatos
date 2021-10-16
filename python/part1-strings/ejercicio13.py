def palindromo(frase: str) -> bool:
    frase_sin_espacios = frase.replace(" ", "")

    frase_lista = [letter.lower() for letter in frase_sin_espacios]
    
    frase_lista_reversed = frase_lista.copy()
    frase_lista_reversed.reverse()

    return frase_lista == frase_lista_reversed

example_palindromo = "Ana lava lana"
example_no_palindromo = "Esto es un gato"

print(f'Con la frase `{example_palindromo}` la función devuelve {palindromo(example_palindromo)}')
print(f'Con la frase `{example_no_palindromo}` la función devuelve {palindromo(example_no_palindromo)}')
