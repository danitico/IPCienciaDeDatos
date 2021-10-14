import unicodedata


example = "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú hispalense"


print(unicodedata.normalize('NFD', example))
