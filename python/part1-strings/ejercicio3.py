def mayusculas_minusculas(palabra: str) -> str:
    return ''.join([letter.lower() if letter.isupper() else letter.upper() for letter in palabra])

example = "EsTo Es Un EjEmPlO"

new_string = mayusculas_minusculas(example)

print(new_string)
