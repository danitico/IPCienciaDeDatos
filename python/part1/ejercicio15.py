def todas_las_letras(palabra: str, letras: str) -> bool:
    return all(letra.upper() in palabra.upper() for letra in letras)

example = "gato"

print(f'Si buscamos las letras ao en la palabra gato la función devuelve {todas_las_letras(example, "ao")}')
print(f'Si buscamos las letras aop en la palabra gato la función devuelve {todas_las_letras(example, "aop")}')
