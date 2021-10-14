def contar_letras(palabra: str, letra: str) -> int:
    return palabra.count(letra)

example = "Esto es un ejemplo"

count = contar_letras(example, 'e')

print(count)
