# Ask the user to introduce with the keyboard a string s and a number n and show in the screen n times
# the string s (without spaces between words) / Pide al usuario que introduzca por teclado un string s
# y un número n y que muestre en pantalla n veces seguidas el string s (sin espacios entre palabra y palabra).

s <- readline("Introduce una cadena: ")
n <- as.numeric(readline("Introduce un numero: "))

paste(replicate(n, s), collapse = "")
