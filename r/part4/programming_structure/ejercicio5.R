# Given a matrix return a list of all values greater than 7 of each row
# Dada una matriz devuelva una lista con los valores mayores a 7 de cada fila.

matriz <- rbind(
  c(1, 2, 3),
  c(3, 6, 9),
  c(11, 13, 1)
)

apply(matriz, 1, function (x) x[x > 7])
