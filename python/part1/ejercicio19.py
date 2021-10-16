def pangrama(frase: str) -> bool:
    NORMAL_MAP = {
        'À': 'A', 'Á': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A',
        'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'ª': 'A',
        'È': 'E', 'É': 'E', 'Ê': 'E', 'Ë': 'E',
        'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
        'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'Ò': 'O', 'Ó': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O',
        'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'º': 'O',
        'Ù': 'U', 'Ú': 'U', 'Û': 'U', 'Ü': 'U',
        'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u',
        'Ñ': 'N', 'ñ': 'n',
        'Ç': 'C', 'ç': 'c',
        '§': 'S',  '³': '3', '²': '2', '¹': '1'
    }

    normalize = str.maketrans(NORMAL_MAP)
    NUMBER_LETTERS_ALPHABET = 26

    formatted_string = frase.translate(normalize)

    formatted_string_set = set([letter.lower() for letter in formatted_string if letter.isalpha()])

    return len(formatted_string_set) == NUMBER_LETTERS_ALPHABET


example = "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"
negative_example = "Es muy temprano"

print(f'Con la frase "{example}" la función devuelve {pangrama(example)}')
print(f'Con la frase "{negative_example}" la función devuelve {pangrama(negative_example)}')
