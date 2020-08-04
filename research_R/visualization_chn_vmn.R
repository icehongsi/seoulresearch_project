library(dplyr)
library(moments)
library(corrplot)
library(MASS)
library(forcats)
library(car)
library(leaps)
library(ggplot2)

data = read.csv(file.choose())
colnames(data)
summary(data)
table(data$h_gu_cd)
data$tt = as.factor(data$tt)
data$h_gu_cd = as.factor(data$h_gu_cd)
str(data)
table(data$tt)
data$isworkhour = fct_collapse(as.factor(data$tt), t = c(as.character(9:18)), f = c(as.character(0:8), as.character(19:23)))

ggplot(data, aes(x = h_gu_cd, y = vnm, fill = isworkhour)) + geom_bar(stat = "identity", position = "dodge")
ggplot(data, aes(x = h_gu_cd, y = chn, fill = isworkhour)) + geom_bar(stat = "identity", position = "dodge")
ggplot(data, aes(x = h_gu_cd, y = jpn, fill = isworkhour)) + geom_bar(stat = "identity", position = "dodge")
ggplot(data, aes(x = h_gu_cd, y = can, fill = isworkhour)) + geom_bar(stat = "identity", position = "dodge")
ggplot(data, aes(x = h_gu_cd, y = twn, fill = isworkhour)) + geom_bar(stat = "identity", position = "dodge")
ggplot(data, aes(x = h_gu_cd, y = usa, fill = isworkhour)) + geom_bar(stat = "identity", position = "dodge")
ggplot(data, aes(x = h_gu_cd, y = etcsum, fill = isworkhour)) + geom_bar(stat = "identity", position = "dodge")
ggplot(data, aes(x = h_gu_cd, y = forsum, fill = isworkhour)) + geom_bar(stat = "identity", position = "dodge")

#import dist code info

distcode = read.table(file.choose(), sep = '\t', header = TRUE, fileEncoding = "UTF-8", quote = "")
distcode
subset(distcode, select =)
read.table()
# resident

proportion = read.table(file.choose(), sep = "\t", stringsAsFactors = FALSE, header = T)
summary(proportion)

proportion = lapply(proportion, FUN = function(x) {if (is.integer(x)) as.numeric(x)})
summary(proportion)
  