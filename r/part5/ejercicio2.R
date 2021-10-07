library(ggplot2)

ex2 <- data.frame(year=c(1970:1979), snow.cover=c(6.5,12.0,14.9,10.0,10.7,7.9,21.9,12.5,14.5,9.2))

ggplot(
  ex2,
  aes(
    x=as.character(year),
    y=snow.cover
  )
) + geom_bar(fill="blue", stat="identity", width = .5) + labs(title="Snow every year", x="Year", y="Snow cover")

ggplot(
  ex2,
  aes(x=snow.cover)
) + geom_histogram(bins = 6) + labs(title="Histogram of snow cover", x="Snow cover")
