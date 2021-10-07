library(ggplot2)

ex1 <- data.frame(stretch=c(46,54,48,50,44,42,52), distance=c(148,182,173,166,109,141,166))

ggplot(ex1, aes(x=stretch, y=distance)) + geom_line() + labs(title="Distance against stretch")
