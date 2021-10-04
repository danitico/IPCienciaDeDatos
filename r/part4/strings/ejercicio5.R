# Given three numeric arrays representing days, months and years, create an array with dates 
# (only if they are valid) (Hint: research the as.Date function) / Dados tres vectores dia, mes
# y año crea un vector con las fechas completas. Si la fecha es inválida, ésta se descartará
# (Ayuda: investiga la función as.Date).

days <- c(2, 32, 28)
months <- c(11, 45, 4)
years <- c(1998, 2002, 1999)

datetimes <- paste(days, months, years, sep='-')

datetimes[
  which(tryCatch(as.Date(datetimes), error = function(err) {FALSE}) != FALSE)
]
