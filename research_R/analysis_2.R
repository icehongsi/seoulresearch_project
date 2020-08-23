install.packages(c("dplyr", "ggplot2", "ISLR", "MASS", "glmnet", "randomForest", "gbm", "rpart", "boot"))

library(readxl)
library(dplyr)
library(ggplot2)
library(ISLR)
library(MASS)
library(glmnet)
library(randomForest)
library(gbm)
library(rpart)
library(boot)
library(corrplot)
library(RColorBrewer)

data = read_excel(file.choose())
data[,c(9:13)] = lapply(data[,c(9:13)], factor)
data = na.omit(data)
data %>% glimpse()

data %>% mutate_at(vars(price), as.double)

wwdata[,14] = lapply(data[,14], numeric)

data.usa = data[,c(8,14:51)]
data.vi = data[,c(9,14:51)]
data.ch = data[,c(10,14:51)]
data.jp = data[,c(11,14:51)]
data.tw = data[,c(12,14:51)]
data.usa
data.tw$univ_count

manova(data[,c(8:12)] ~ data[,c(14:51)])

data %>% glimpse()
corrplot(as.matrix(cor(data[,c(38:44)])))
corrplot(as.matrix(cor(dplyr::select_if(data, is.numeric) %>% na.omit())), is.corr = FALSE)





ch.tree = rpart(hot_ch ~ ., data = data.ch)

opar = par(mfrow = c(1,1), xpd = NA)
ch.tree %>% printcp()
ch.tree %>% plot()
text(ch.tree, use.n = T)
par(opar)

data.ch.rf = randomForest(hot_ch ~ ., data = data.ch)
data.ch.rf
plot(data.ch.rf)

tmp = importance(data.ch.rf)
head(round(tmp[order(-tmp[,1]), 1, drop = F], 2), n = 10)
varImpPlot(data.ch.rf)

data = read_excel(file.choose())

data %>% glimpse()

lm(data.frame(data[,13]) ~ data.frame(data[, 14:51]), data = data)

lm(hot_usa ~ dplyr::select(data, ("price":"sum")), data = data)

data[bynation] = lapply(data[bynation], factor)

data_numeric = dplyr::select_if(data, is.numeric)


length(data_numeric)

do.call(rbind.data.frame, data_numeric)


typeof(data_numeric)
corrplot(as.matrix(cor(dplyr::select_if(data, is.numeric) %>% na.omit())), is.corr = FALSE)


bynation = c("hot_usa", "hot_vi", "hot_ch", "hot_jp", "hot_cn")

nation = data[,colnames(data) %in% bynation]




hist(log1p(data$bank_sum))
data %>% glimpse()
lm(daga_percent ~ bank_sum, data = data, na.action = na.omit) %>% summary()
plot(daga_percent~bank_sum, data = data)
abline(a = -0.005522, b = 0.367775)


data[, !colnames(data) %in% bynation]










lm.model = lm(population ~ . -adm_nm, data = data)
summary(lm.model)

data_rf = randomForest(population ~. - adm_nm, data = data)
data_rf
plot(data_rf)

data_gbm = gbm(population ~. - adm_nm, data = data, n.trees = 40000, cv.folds = 3, verbose = TRUE)
summary(data_gbm)

data.rpart = rpart(population ~. - adm_nm, method = "class")
