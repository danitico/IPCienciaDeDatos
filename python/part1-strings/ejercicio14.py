def orden_alfabetico(palabra: str) -> bool:
    palabra_lista = [letter for letter in palabra]
    palabra_lista_ordenada = palabra_lista.copy()

    palabra_lista_ordenada.sort()

    return palabra_lista == palabra_lista_ordenada

example_no_ordenado = 'gato'
example_ordenado = 'abejo'

print(f'Con la palabra {example_no_ordenado} la función devuelve {orden_alfabetico(example_no_ordenado)}')
print(f'Con la palabra {example_ordenado} la función devuelve {orden_alfabetico(example_ordenado)}')
