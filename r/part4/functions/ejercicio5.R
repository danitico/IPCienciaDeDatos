# Create a function that given an array v and two values x and y (with y an optional parameter), returns a new array with
# the values included after the first x up to the first y. If y is not indicated, the function will return the values after
# the first x until the end of the array / Crea una función partir que dado un vector v y dos valores x e y (siendo y opcional),
# retorne un vector con los valores que aparecen luego del primer x y hasta el primer y. De no indicarse el valor de y se
# devolveran todos los valores que aparecen luego del primer x hasta el final del vector.

sliceArray <- function(v, x, y=-1) {
  if (y == -1) {
    y <- length(v)
  }

    v[(x+1):y]
}

anArray <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliceArray(anArray, 1, 5)
sliceArray(anArray, 1)
