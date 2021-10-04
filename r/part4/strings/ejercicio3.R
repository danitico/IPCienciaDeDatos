# Given a string with several words (e.g., “Esta es una frase, pero no cualquier frase.”)
# create an array with each of the words in the string (e.g., ["Esta","es","una","frase","pero","no","cualquier","frase"])
# Dado un string con varias palabras (e.g., “Esta es una frase, pero no cualquier frase.”)
# crea un vector con cada una de las palabras del string (e.g., ["Esta","es","una","frase","pero","no","cualquier","frase"]).

sentence <- "Esta es una frase pero no cualquier frase."

strsplit(sentence, split="[ |\\.]")

