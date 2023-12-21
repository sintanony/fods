import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Using Python code for the mtcars dataset to plot the correlation matrix
# Replace "path-to-the-file/mtcars.csv" with the correct path to your mtcars dataset file
df = pd.read_csv(r'N:\Education\coding_code\python\mtcars.csv')

# Drop non-numeric columns (e.g., 'car_names') before calculating the correlation matrix
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Correlation Matrix
cor_matrix = numeric_df.corr(method="pearson")
print("Correlation Matrix:")
print(cor_matrix)

# Covariance Plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))
cov_plot = sns.scatterplot(data=df, x="mpg", y="cyl", hue="gear", palette="viridis", size="hp", sizes=(10, 200))
cov_plot.set_title("Covariance Plot: mpg vs cyl")
plt.show()