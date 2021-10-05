# Given two numbers, f and c, introduced using the keyboard by the user, create a square of f rows and c collumns with
# character "x"./ Dados dos números introducidos por el usuario f y c, crea un cuadrado de f filas y c columnas con el 
# caracter "x"

f <- readline("Introduce el número de filas: ")
c <- readline("Introduce el número de columnas: ")

f <- as.numeric(f)
c <- as.numeric(c)

matriz1 <- matrix("x", nrow = f, ncol = c)

write.table(matriz1, sep = "", row.names = F, col.names = F, quote = F)
