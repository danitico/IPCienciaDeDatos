def buscar(palabra: str, sub: str) -> int:
    return palabra.find(sub)

example = "Esto es un ejemplo"

position = buscar(example, 'es')

print(position)
