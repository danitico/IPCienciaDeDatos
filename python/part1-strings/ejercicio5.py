def num_vocales(palabra: str) -> int:
    return len([letter for letter in palabra if letter.upper() in "AEIOU"])

example = "Esto es un ejemplo"

number_vowels = num_vocales(example)

print(number_vowels)
