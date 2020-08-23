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
data[bynation] = lapply(data[bynation], factor)
summary(data)
glimpse(data)


data_numeric = dplyr::select_if(data, is.numeric)

data_numeric
length(data_numeric)

do.call(rbind.data.frame, data_numeric)


typeof(data_numeric)
corrplot(dplyr::select_if(data, is.numeric), type ="upper", orer = "hclust")


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
