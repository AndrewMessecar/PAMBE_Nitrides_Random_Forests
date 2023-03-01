# Andrew S. Messecar
# 2023

library(randomForest)

Data = read.csv("# Training Data File Path", header=T)

attach(Data)

# fix(Data)

bag <- randomForest(Crystal~., data=Data)

plot(bag)