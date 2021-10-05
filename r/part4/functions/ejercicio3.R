# Create a function "unir" that given two arrays returns a new array with the elements of both arrays without repetition
# Crea una función "unir" que dados dos vectores devuelva un nuevo vector con los elementos de ambos vectores sin repetidos.

unir <- function (x, y) {
  unique(c(x, y))
}

x <- c(1, 2, 3)
y <- c(2, 3, 4)

unir(x, y)
