# Loading the Iris dataset
data(iris)
iris2 <- iris

# Histogram of Sepal Length
hist(iris2$Sepal.Length, main="Histogram of Sepal Length", xlab="Sepal Length", xlim=c(4, 8), col="blue", freq=FALSE)

# Histogram of Sepal Width
hist(iris2$Sepal.Width, main="Histogram of Sepal Width", xlab="Sepal Width", xlim=c(2, 5), col="darkorchid", freq=FALSE)

# Creating subsets for each species
irisVer <- subset(iris, Species == "versicolor")
irisSet <- subset(iris, Species == "setosa")
irisVir <- subset(iris, Species == "virginica")

# Boxplots for each species
par(mfrow=c(1, 3), mar=c(6, 3, 2, 1))
boxplot(irisVer[,1:4], main="Versicolor, Rainbow Palette", ylim=c(0, 8), las=2, col=rainbow(4))
boxplot(irisSet[,1:4], main="Setosa, Heat color Palette", ylim=c(0, 8), las=2, col=heat.colors(4))
boxplot(irisVir[,1:4], main="Virginica, Topo colors Palette", ylim=c(0, 8), las=2, col=topo.colors(4))
