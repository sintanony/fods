# Using R code for the Iris dataset to plot the correlation matrix between sepal width and sepal length
library(datasets)
data(iris)

# Correlation Plot
plot(iris)

# Correlation Matrix
cor_matrix <- cor(iris[, 1:4])
cat("Correlation Matrix:\\n")
print(cor_matrix)

# Scatter plot for sepal width vs sepal length
print(plot(iris$Sepal.Width, iris$Sepal.Length, main="Scatter Plot: Sepal Width vs Sepal Length", xlab="Sepal Width", ylab="Sepal Length", pch=19, col=iris$Species))
