# Given an array of strings representing dates (e.g., [“2005-11-28”, “2015-10-18”, “2000-01-01”]),
# show only those corresponding to odd months / Dado un vector de fechas, expresadas como strings
# (e.g., [“2005-11-28”, “2015-10-18”, “2000-01-01”]), muestra solamente aquellas correspondientes
# a los meses impares.

random_dates = c("2005-11-28", "2015-10-18", "2000-01-01")

random_dates[
  which(
    as.numeric(format(as.Date(random_dates), "%m")) %% 2 != 0
  )
]
