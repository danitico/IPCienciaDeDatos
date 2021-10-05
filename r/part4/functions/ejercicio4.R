# Create a function "vyc" that given a string returns a list of two components, one containing the vowels and the
# other the consonants / Crea una función "vyc" que dado un string devuelva una lista de dos componentes que contenga
# las vocales y las consonantes.

vyc <- function(string) {
  list(
    vocales=gsub("[^aeiouAEIOU]", "", meow),
    consonantes=gsub("[A|E|I|O|U|a|e|i|o|u| ]", "", meow)
  )
}

aString = "Esto es un gato"

vyc(aString)
