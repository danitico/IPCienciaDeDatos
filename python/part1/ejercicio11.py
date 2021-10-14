def comunes(palabra1: str, palabra2: str) -> str:
    palabra1_set = {letter for letter in palabra1}
    palabra2_set = {letter for letter in palabra2}

    return ''.join(palabra1_set.intersection(palabra2_set))

palabra1 = "brisa"
palabra2 = "parabrisas"

common_letters = comunes(palabra1, palabra2)

print(common_letters)
