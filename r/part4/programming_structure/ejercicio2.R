# Create a function "montecarlo" that calculates the estimation of the given integral
# Crea una función "montecarlo" que calcule la estimación de la siguiente integral

montecarlo <- function(n=10000) {
  sum(
    ifelse(
      runif(n) < (runif(n)**2), 1, 0
    )
  )/n 
}

montecarlo()
