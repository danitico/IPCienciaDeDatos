# Calculate the minimum value of each column of a matrix, but assume odd numbers are negative and even numbers are positive
# Calcula el valor mínimo de cada columna de una matriz, pero toma los valores impares como numeros negativos y los pares como positivos.

specialMin <- function(x) {
  min(ifelse(x %% 2 == 0, x, -x))
}

matriz <- rbind(
  c(1, 4, 1),
  c(2, 6, 3),
  c(4, 8, 5)
)

apply(matriz, 2, specialMin)
