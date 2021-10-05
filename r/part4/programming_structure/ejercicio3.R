# Create a list of five numeric arrays and order them after its creation
# Crea una lista de 5 vectores numéricos y ordena todos los vectores de la lista.

lista <- list(vector1=c(4, 3, 2, 1), vector2=c(3, 2, 1), vector3=c(5, 4, 3, 2, 1), vector4=c(2, 1), vector5=c(3, 1))

listaOrdenada <- lapply(lista, sort)
listaOrdenada
