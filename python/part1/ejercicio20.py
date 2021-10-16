def encriptar(cad: str, desp: int) -> str:
    # remove accents
    NORMALISATION_MAP = {
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

    normalize = str.maketrans(NORMALISATION_MAP)
    formatted_cad = cad.translate(normalize)
    offset_upper_letters_ascii = 65
    offset_lower_letters_ascii = 97

    encrypted_list = [
        letter
        if not letter.isalpha()
        else (
            chr((ord(letter) + desp - offset_upper_letters_ascii) % 26 + offset_upper_letters_ascii)
            if letter.isupper()
            else chr((ord(letter) + desp - offset_lower_letters_ascii) % 26 + offset_lower_letters_ascii)
        )
        for letter in formatted_cad
    ]

    return ''.join(encrypted_list)


example = "Es muy temprano"

print(encriptar(example, 13))
