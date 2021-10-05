# Load the three files created in the last exercise and create a matrix with three columns,
# one for each file conent / Carga los tres ficheros creados en el punto anterior y construye
# una matriz que, en cada columna, tengo el contenido de cada fichero.

twoTable <- scan("dos.txt", what=numeric())
threeTable <- scan("tres.txt", what=numeric())
fiveTable <- scan("cinco.txt", what=numeric())

matrix(c(twoTable, threeTable, fiveTable), ncol = 3)
