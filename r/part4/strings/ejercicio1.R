# Create a string array contaning your first name and last names (e.g., ["Rocio", "Romero", Zaliz"]). 
# Using that array and the R functions you just learned create a new string with the initial of your first name,
# a dot, and your last names (e.g., "R. Romero Zaliz") / Crea un vector de strings con tu primer nombre y tus dos
# apellidos. A partir de éste crea un nuevo string con la inicial de tu nombre (y un punto) y el apellido completo
# utilizando lo aprendido anteriormente. En mi caso debería quedar: "R. Romero Zaliz".

fullname <- c("Daniel", "Ranchal", "Parrado")
paste(
  paste(
    substr(fullname[1], 1, 1),
    "."
  ),
  fullname[2],
  fullname[3]
)
