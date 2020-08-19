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

data = read_excel(file.choose())
summary(data)
glimpse(data)

lm.model = lm(population ~ . -adm_nm, data = data)
summary(lm.model)

data_rf = randomForest(population ~. - adm_nm, data = data)
data_rf
plot(data_rf)

data_gbm = gbm(population ~. - adm_nm, data = data, n.trees = 40000, cv.folds = 3, verbose = TRUE)
summary(data_gbm)

data.rpart = rpart(population ~. - adm_nm, method = "class")
