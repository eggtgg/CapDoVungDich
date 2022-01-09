# get means for variables in data frame mydata
# excluding missing values
setwd('C:\\Users\\Dell\\mtri_egg\\capdovungdich')
df <- read.csv("ban_mau_2.csv", encoding = "UTF-8", header = TRUE)
length(df$cap)
table(df$cap)/length(df$cap)
