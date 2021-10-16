def eco_palabra(palabra: str) -> str:
    return palabra * len(palabra)

example = "gato"

new_string = eco_palabra(example)

print(new_string)
