# Create three files called dos.txt, tres.txt and cinco.txt containing the table of 2, 3 and 5
# respectively (the first 10 values of each, one number at a time) / Crea tres ficheros llamados dos.txt,
# tres.txt y cinco.txt que contenga la tabla del 2, la del 3 y la del 5 respectivamente (los primeros 10
# valores de cada tabla, un número en cada línea de cada fichero)

write.table(matrix(seq(from=2, by=2, length.out = 10), ncol = 1), "dos.txt", row.names = F, col.names = F)
write.table(matrix(seq(from=3, by=3, length.out = 10), ncol = 1), "tres.txt", row.names = F, col.names = F)
write.table(matrix(seq(from=5, by=5, length.out = 10), ncol = 1), "cinco.txt", row.names = F, col.names = F)
