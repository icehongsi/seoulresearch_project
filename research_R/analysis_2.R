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
data[,c(3:8)] = lapply(data[,c(3:8)], factor)
data = na.omit(data)
data %>% glimpse()

data.canada = data[,c(3,9:31)]
data.china = data[,c(4,9:31)]
data.japan = data[,c(5,9:31)]
data.taiwan = data[,c(6,9:31)]
data.us = data[,c(7,9:31)]
data.vietnam = data[,c(8,9:31)]
data.us
data.ch
corrplot(as.matrix(cor(data[,c(38:44)])))
corrplot(as.matrix(cor(dplyr::select_if(data, is.numeric) %>% na.omit())), is.corr = FALSE)


data.us
glm.us
glm.us = glm(us_hsp ~ ., data = data.us, family = binomial)
glm.ch = glm(china_hsp ~ ., data = data.china, family = binomial)
glm.ca = glm(canada_hsp ~ ., data = data.canada, family = binomial)
glm.vi = glm(vietnam_hsp ~ ., data = data.vietnam, family = binomial)
glm.jp = glm(japan_hsp ~ ., data = data.japan, family = binomial)
glm.tw = glm(taiwan_hsp ~., data = data.taiwan, family = binomial)

glm.us %>% summary()
glm.us$model

us.aic.result = stepAIC(glm.us, direction = "both") %>% plot()
#us.aic.result# %>% summary()
ch.aic.result = stepAIC(glm.ch, direction = "both")
ca.aic.result = stepAIC(glm.ca, direction = "both")
vi.aic.result = stepAIC(glm.vi, direction = "both")
jp.aic.result = stepAIC(glm.jp, direction = "both")
tw.aic.result = stepAIC(glm.tw, direction = "both")

us_x = model.matrix(us_hsp ~ . -1, data.us)
y = data.us$us_hsp
ad_glmnet_fit = glmnet(us_x, y, family = "binomial")
plot(ad_glmnet_fit)

cv.glmnet.fit = cv.glmnet(us_x, y, family = "binomial")
plot(cv.glmnet.fit)
cv.glmnet.fit







gbm(us_hsp ~., data = data.us, distribution = "bernoulli", n.trees = 50000, cv.folds = 3, verbose = TRUE)


ch.tree = rpart(china_hsp ~ ., data = data.ch)
opar = par(mfrow = c(1,1), xpd = NA)
ch.tree %>% printcp()
ch.tree %>% plot()
text(ch.tree, use.n = T)
par(opar)

data.ch.rf = randomForest(china_hsp ~ ., data = data.ch)
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
