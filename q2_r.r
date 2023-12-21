# Using tidyverse for data manipulation
library(tidyverse)

# Importing the Iris dataset
data("iris")
iris_copy <- iris

# Introducing missing values in some columns
iris_copy$Sepal.Length[c(15, 20, 50, 67, 97, 118)] <- NA
iris_copy$Sepal.Width[c(4, 80, 97, 106)] <- NA
iris_copy$Petal.Length[c(5, 17, 35, 49)] <- NA

# Displaying missing values summary
cat("Summary with Missing Values:\\n")
print(summary(iris_copy))

# Dropping rows with missing values
iris_clean <- na.omit(iris_copy)

# Displaying cleaned data
cat("\\nCleaned Data:\\n")
print(iris_clean)
