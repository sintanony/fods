# Using R code to implement PCA for the Iris dataset
library(datasets)
data("iris")
library(caret)

# Splitting the data into training and testing sets
set.seed(100)
ind <- createDataPartition(iris$Species, p=0.80, list=FALSE)
train <- iris[ind, ]
test <- iris[-ind, ]

# PCA
pc <- prcomp(train[, -5], center=TRUE, scale=TRUE)
summary(pc)

# Scatter plot for the first three principal components
pairs.panels(pc$x, gap=0, bg=c("red", "blue", "yellow")[train$Species], pch=21)
