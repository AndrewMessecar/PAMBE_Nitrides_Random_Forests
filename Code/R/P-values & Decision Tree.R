# Andrew S. Messecar
# 2023

library(rpart)
library(rpart.plot)

Data = read.csv("# Training Data File Path", header=T)

attach(Data)

# fix(Data)

glm.fits=glm(Crystal~., data=Data, family=binomial)

summary(glm.fits)

tree_Data <- rpart(Crystal~., data=Data)

rpart.plot(tree_Data)