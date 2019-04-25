# Code to find the outliers in NASA Dataset

mydata <- read.csv("~/Spring 2019/Semantic Web Mining/Final project Demo/julydata200.csv", header=TRUE)
tempUTC <- mydata
names(tempUTC)
head(tempUTC)
tempUTC[1:5] <- list(NULL)
names(tempUTC)
pairs(tempUTC, main= "the pairs() command" )