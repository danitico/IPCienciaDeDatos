# Create a function "impares" that given an array returns the number of odd elements it contains
# Crea una función "impares" que dado un vector devuelva la cantidad de elementos impares que contiene.

impares <- function(x) {
  sum(ifelse(x %% 2 == 1, 1, 0))
}

x <- c(1, 2, 3, 4, 5)

impares(x)
