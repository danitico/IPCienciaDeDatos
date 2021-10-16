def inicio_fin_local(palabra: str) -> bool:
    vowels = "AEIOU"

    if not palabra:
        return False

    return palabra[0].upper() in vowels and palabra[-1].upper() in vowels

print(f'La palabra Gato devuelve {inicio_fin_local("gato")}')
print(f'La palabra Alhambra devuelve {inicio_fin_local("Alhambra")}')
