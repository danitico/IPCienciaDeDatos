def vocales(palabra: str) -> str:
    return ''.join([letter for letter in palabra if letter.upper() in "AEIOU"])

example = "Esto es un ejemplo"

string_vowels = vocales(example)

print(string_vowels)
