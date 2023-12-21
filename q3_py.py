import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'N:\\Education\\coding_code\\python\\iris.csv')

# Displaying the mean and median for each species
agg_stats = df.groupby('species').agg(['mean', 'median'])
print(agg_stats)

# Distribution plot for petal width
sns.distplot(a=df['petal_width'], bins=40, color='b')
plt.title('Petal Width Distribution Plot')
plt.show()

# Count of number of observations of each species
sns.countplot(x='species', data=df)
plt.title('Count of Observations for Each Species')
plt.show()

# Pairplot for all variables
sns.pairplot(df, hue='species')
plt.title('Pairplot for Iris Dataset')
plt.show()

# Scatter plot for sepal length and sepal width
plt.figure(figsize=(17, 9))
plt.title("Comparison between various species based on sepals' length and width")
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df, s=50)
plt.show()