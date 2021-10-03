library(datasets)

# dimensiones dataframe
dim(USArrests)

# Numero columnas
nrow(USArrests)

# Numero filas
ncol(USArrests)

# Ordenar filas por porcentaje población urbana

USArrests[order(USArrests$UrbanPop, decreasing = TRUE),]

# Ordenar filas por porcentaje poblacion y asesinatos

USArrests[order(USArrests$UrbanPop, USArrests$Murder, decreasing = TRUE),]

# Mostrar asesinatos
print(USArrests$Murder)

# Muestra las tasas de asesinato para el segundo, tercer y cuarto estado
print(USArrests$Murder[2:4])

# Muestra las primeras cinco filas de todas las columnas
print(USArrests[1:5,])

# Muestra todas las filas para las dos primeras columnas
print(USArrests[, 1:2])

# Muestra todas las filas de las columnas 1 y 3
print(USArrests[, c(1, 3)])

# Muestra solo las primeras cinco filas de las columnas 1 y 2
print(USArrests[1:5,1:2])

# Extrae las filas para el índice Murder
print(USArrests$Murder)

# Que estado tiene la menor tasa de asesinatos? ¿qué línea contiene esa información?, obtén esa información
x <- USArrests[which.min(USArrests$Murder),]
rownames(x)


# ¿Que estados tienen una tasa inferior al 4%?
rownames(USArrests[USArrests$Murder < 4,])

# ¿Que estados estan en el cuartil superior (75) en lo que a poblacion en zonas urbanas se refiere?
rownames(USArrests[USArrests$UrbanPop >= quantile(USArrests$UrbanPop)[4],])


