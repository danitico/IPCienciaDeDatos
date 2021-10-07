library(readr)
library(dplyr)
library(ggplot2)

FtoC <- function(x) {
  (x - 32)/1.8
}

inchesToMilimeters <- function(x) {
  x*25.4
}

df <- read_csv("dataset.csv")

df <- df %>% mutate(
  LowestTemperature=FtoC(`Lowest Temperature (F)`),
  HighestTemperature=FtoC(`Highest Temperature (F)`),
  WarmestMinimumTemperature=FtoC(`Warmest Minimum Temperature (F)`),
  ColdestMinimumTemperature=FtoC(`Coldest Minimum Temperature (F)`),
  AverageMaximumTemperature=FtoC(`Average Maximum Temperature (F)`),
  AverageMinimumTemperature=FtoC(`Average Minimum Temperature (F)`),
  MeanTemperature=FtoC(`Mean Temperature (F)`),
  TotalPrecipitation=inchesToMilimeters(`Total Precipitation (in)`),
  TotalSnowfall=inchesToMilimeters(`Total Snowfall (in)`),
  Max24hrPrecipitation=inchesToMilimeters(`Max 24hr Precipitation (in)`),
  Max24hrSnowfall=inchesToMilimeters(`Max 24hr Snowfall (in)`),
  `Lowest Temperature (F)`=NULL,
  `Highest Temperature (F)`=NULL,
  `Warmest Minimum Temperature (F)`=NULL,
  `Coldest Minimum Temperature (F)`=NULL,
  `Average Maximum Temperature (F)`=NULL,
  `Average Minimum Temperature (F)`=NULL,
  `Mean Temperature (F)`=NULL,
  `Total Precipitation (in)`=NULL,
  `Total Snowfall (in)`=NULL,
  `Max 24hr Precipitation (in)`=NULL,
  `Max 24hr Snowfall (in)`=NULL,
)

ggplot(
  df,
  aes(
    x=Year,
    y=WarmestMinimumTemperature,
    group = 1
  )
) + geom_line() + labs(title="Warmest minimun temperature along the years", y="Warmest Minimun Temperature", x="Year") + scale_x_continuous(breaks=seq(1900, 2014, 10))


ggplot(df, aes(x=Year)) + geom_line(
  aes(y=WarmestMinimumTemperature, colour="Warmest Minimum Temperature")
) + geom_line(
  aes(y=ColdestMinimumTemperature, colour="Coldest Minimum Temperature")
) + scale_colour_manual(
  values = c("Warmest Minimum Temperature" = "blue", "Coldest Minimum Temperature" = "red")
) + labs(
  title="Temperature along the years",
  y="Temperature",
  x="Year"
) + scale_x_continuous(breaks=seq(1900, 2014, 10))


