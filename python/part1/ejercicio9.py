def elimina_vocales(palabra: str) -> str:
    return ''.join([letter for letter in palabra if letter.upper() not in "AEIOU"])


example = "Esto es un ejemplo"

new_string = elimina_vocales(example)

print(new_string)
