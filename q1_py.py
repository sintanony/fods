import pandas as pd

# Importing the Iris dataset
df = pd.read_csv(r'N:\Education\coding_code\python\iris.csv')

# Displaying head, tail, summary, info, and interquartile range
print("Head:")
print(df.head())

print("\\nTail:")
print(df.tail())

print("\\nSummary:")
print(df.describe())

print("\\nInfo:")
print(df.info())

# Select numeric columns only
numeric_df = df.select_dtypes(include=['float64', 'int64'])

print("\nInterquartile Range (Q3 - Q1):")
print(numeric_df.quantile(0.75) - numeric_df.quantile(0.25))