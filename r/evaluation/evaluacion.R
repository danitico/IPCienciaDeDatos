library(tidyverse)
library(ggplot2)

# FRECUENCIA DE LAS PALABRAS

## Get contents of the file and convert it to dataframe
filePointer = file("fichero.txt", open="r")
lines <- readLines(filePointer, warn = F)
close(filePointer)
df <- as.data.frame(lines)

## Rename columns, remove punctuation, transform to lowercase and split text of each line into a vector
## of words
df <- df %>% rename(
  words_list=lines
) %>% mutate(
  line_number=1:dim(df)[1],
  words_list = str_split(
    str_to_lower(
      str_replace_all(words_list, "[:punct:]", "")
    ),
    " "
  )
)

## Unnest the text variable, which is a vector, into several rows
## After that operation, each row will be a word
## Then we remove the blank words, group by word and generate per each word
## their appeareance in a column called lines
words <- df %>% rename(
  word=words_list
) %>% unnest_longer(
  word
) %>% filter(
  word != ""
) %>% group_by(
  word
) %>% nest(
  lines = c(line_number)
)

## Obtenemos la lista de las líneas en las que aparece la palabra
## y el número de veces que aparece por cada línea en forma de lista
## Se crea la variable total_count, que es la suma de los elementos del vector lines_count_list
## y se calcula la longitud de la palabra en la variable length. Se cambia el orden de la variable
## length después de la variable word
words <- words %>% rowwise() %>% mutate(
  lines_ocurrences_list = list(as.numeric(names(table(lines)))),
  lines_count_list = list(as.numeric(table(lines)))
) %>% mutate(
  total_count = sum(lines_count_list),
  lines = NULL,
  length = str_length(word)
) %>% relocate(length, .after = word)

words

## Write word frequency to csv
words %>% mutate(
  lines_ocurrences_list = paste(lines_ocurrences_list, collapse = ";"),
  lines_count_list = paste(lines_count_list, collapse = ";")
) %>% write_csv("word_frequency.csv")

# GRAFICOS
## Número de la palabras únicas por linea
words %>% unnest_longer(
  lines_ocurrences_list
) %>% ggplot(
  aes(x = lines_ocurrences_list)
) + geom_histogram(
  bins = dim(df)[1]*2
) + scale_x_continuous(
  breaks = 1:dim(df)[1]
) + labs(
  x = "Línea",
  y="Número de palabras únicas por línea"
) + theme(axis.text.x=element_text(angle=90, hjust=1))

## Frecuencia de las palabras por línea
words %>% unnest(
  cols = c(lines_ocurrences_list, lines_count_list)
) %>% ggplot(
  aes(x=word, y=lines_count_list)
) + geom_col() + facet_wrap(
  ~ lines_ocurrences_list, scales = "free"
) + theme(axis.text.x=element_text(angle=90, hjust=1))

## word cloud
words %>% ggplot(
  aes(x=seq_along(total_count), y=total_count, size=total_count, label = word)
) + geom_text(show.legend = F, position = position_jitter(1,1)) + theme(
  axis.line=element_blank(),
  axis.text.x=element_blank(),
  axis.text.y=element_blank(),
  axis.ticks=element_blank(),
  axis.title.x=element_blank(),
  axis.title.y=element_blank()
)


# BIGRAMAS
lines <- read_file("fichero.txt")
fileStringdf = as.data.frame(lines)

# Primero de todo convertimos todo el texto a minúscula
# Dividimos el texto entero por frases. Por eso se hace un str split por punto
# A continuación se hace un unnest_longer para que el vector de frases
# se deshaga y que cada item ocupe una fila
# Luego se eliminan los signos de puntuacion con str_replace_all
# se eliminan espacios y \n redudantes entre palabras y al principio y al final de cada clase
# Finalmente se borran aquellas lineas vacias y se crea un vector
# con str_split utilizando " " como separador
bigrams <- fileStringdf %>% mutate(
  lines=str_to_lower(lines)
) %>% mutate(
  lines=str_split(lines, pattern = "\\.")
) %>% unnest_longer(
  lines
) %>% mutate(
  lines = str_replace_all(lines, "[:punct:]", "")
) %>% mutate(
  lines=str_trim(lines,"both")
) %>% filter(
  lines != ""
) %>% mutate(
  lines=str_replace_all(lines, "[:space:]{2,}|\\n", " "),
) %>% mutate(
  lines=str_split(lines, " ")
)

# A continuación, por cada fila, que representa una frase en forma de vector
# se generan bigramas. Para trabajar con un vector dentro de una celda
# hay que utilizar rowwise y a continuacion, se aplica un sapply
# al que se le pasa un vector con la longitud del vector de la frase
# y se genera una lista de bigramas.
# Luego cada bigrama de las distintas listas, se convierten en filas.
# Se hace un rename la variable a rename y se borran aquellos 
bigrams <- bigrams %>% rowwise() %>% mutate(
  lines=list(
    sapply(
      seq_len(length(lines)),
      function (x) {
        if ((x + 1) <= length(lines)) {
          lines[x:(x+1)]
        }
      }
    )
  )
) %>% unnest_longer(
  lines
) %>% rename(
  bigram=lines
) %>% rowwise() %>% filter(
  is.null(bigram) != T
)

# Finalmente, se convierte el vector bigrama en un string, se agrupa por bigram
# se cuenta el numero de veces que aparece ese bigrama, y por último,
# para no tener bigramas repetidos, se hace un distinct de bigrama manteniendo todas las variables
# del dataframe
bigrams <- bigrams %>% mutate(
  bigram = paste(bigram, collapse = " ")
) %>% group_by(
  bigram
) %>% mutate(
  count = n()
) %>% distinct(
  bigram, .keep_all = T
)

bigrams
