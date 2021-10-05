# Create a function "cambio" that, given a matrix of integer numbers, replaces all NA by 0
# Crea una función "cambio" que dada una matriz de numeros enteros reemplaze todos los NA por el valor 0.

cambio <- function(matriz) {
  matriz[is.na(matriz)] <- 0
  matriz
}

matriz <- rbind(c(NA, 2, NA), c(4, NA, 6))

cambio(matriz)
