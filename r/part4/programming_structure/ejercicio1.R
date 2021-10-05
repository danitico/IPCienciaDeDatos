# Create an increasing function that indicates whether the elements of a given array are strictly increasing.
# Ordering the vector is not allowed / Crea una función creciente que indique si los elementos de un vector
# dado son estrictamente crecientes.No se permite ordenar el vector.

creciente <- function(x) {
  # Apply less or equal operation
  matriz <- outer(x, x, "<=")
  
  # Then, we take the upper triangle of the matrix and they must be all true if the array is in order 
  upperTriangle <- matriz[upper.tri(matriz)]
  all(upperTriangle)  
}

x <- c(2, 1, 3, 5, 4)

if (creciente(x)) {
  print("El vector está ordenado")
} else {
  print("El vector no está ordenado")
}
