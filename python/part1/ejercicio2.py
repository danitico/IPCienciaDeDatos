def eliminar_letras(palabra: str, letra: str) -> str:
    return ''.join([letter for letter in palabra if letter.upper() != letra.upper()])

example = "Esto es un ejemplo"

new_string = eliminar_letras(example, 'e')

print(new_string)
