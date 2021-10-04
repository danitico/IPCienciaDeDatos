# Search in an array of strings those including only vocals "a" and "e"
# Busca las palabras que usan solamente las vocales “a” y “e” en un vector de strings.

aSentence <- c("La", "ciencia", "es", "para", "todos")
aSentence[grep("[ae]", aSentence)]
