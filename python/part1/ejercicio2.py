def eliminar_letras(palabra: str, letra: str) -> str:
    return palabra.replace(f'{letra}', '').replace(f'{letra.upper()}', '')

example = "Esto es un ejemplo"

new_string = eliminar_letras(example, 'e')

print(new_string)
