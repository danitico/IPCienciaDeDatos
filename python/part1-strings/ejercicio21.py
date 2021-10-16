def suma_digitos(cad: str) -> int:
    count = 0

    for letter in cad:
        try:
            count += int(letter)
        except ValueError: # string can not be cast to a integer
            continue

    return count

def suma_digitos_enteros(numero: int) -> int:
    return suma_digitos(str(numero))


example_string = "123456"
example_string_exception = "12a456"
example_number = 123456

print(f'Con la string "{example_string}" la función suma_digitos devuelve {suma_digitos(example_string)}')
print(f'Con la string "{example_string_exception}" la función suma_digitos devuelve {suma_digitos(example_string_exception)}')
print(f'Con el número {example_number} la función suma_digitos_enteros devuelve {suma_digitos_enteros(example_number)}')
