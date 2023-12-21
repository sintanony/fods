# Use R code to implement chi-square test
dat <- iris
dat$size <- ifelse(dat$Sepal.Length < median(dat$Sepal.Length), "small", "big")

# Visualize the relationship between Species and size
library(ggplot2)
ggplot(dat) +
  aes(x = Species, fill = size) +
  geom_bar() +
  scale_fill_hue() +
  theme_minimal()

# Chi-square test
test <- chisq.test(table(dat$Species, dat$size))
test_statistic <- test$statistic
p_value <- test$p.value

# Print results
cat('Chi-square test statistic:', test_statistic, '\\n')
cat('P-value:', p_value, '\\n')

# Summary
summary(table(dat$Species, dat$size))
