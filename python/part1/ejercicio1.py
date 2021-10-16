def contar_letras(palabra: str, letra: str) -> int:
    count = 0

    for letter in palabra:
        if letter.upper() == letra.upper():
            count += 1

    return count

example = "Esto es un ejemplo"

count = contar_letras(example, 'e')

print(count)
