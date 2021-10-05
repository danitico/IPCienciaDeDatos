# Write the first five rows of the matrix created in the last exercise in a new file called prime.txt and the last five in
# another file called fin.txt. Both files must have the data separated by commas / Escribe las cinco primera filas de matriz
# del ejercicio anterior en un fichero nuevo llamado prime.txt y las cinco últimas en otro fichero llamado fin.txt. Ambos
# ficheros deben tener los datos separados por comas.

twoTable <- scan("dos.txt", what=numeric())
threeTable <- scan("tres.txt", what=numeric())
fiveTable <- scan("cinco.txt", what=numeric())

matriz <- matrix(c(twoTable, threeTable, fiveTable), ncol = 3)

prime <- matriz[1:5,]
fin <- matriz[6:10,]

write.table(prime, "prime.txt", sep=",", row.names = F, col.names = F)
write.table(fin, "fin.txt", sep=",", row.names = F, col.names = F)
