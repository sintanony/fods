import pandas as pd

# Importing the Iris dataset
df = pd.read_csv(r'N:\Education\coding_code\python\iris.csv')

# Displaying missing values
print("Missing Values:")
print(df.isnull().sum())

# Dropping unused attribute 'Id'
if 'Id' in df.columns:
    df.drop(columns="Id", inplace=True)
else:
    print("Column 'Id' does not exist in DataFrame")

# Displaying missing values after dropping 'Id'
print("\\nMissing Values after dropping 'Id':")
print(df.isnull().sum())

# Handling missing values using median imputation for numeric columns and mode for non-numeric columns
for column in df.columns:
    if df[column].dtype == 'object':  # if column is non-numeric
        df[column].fillna(df[column].mode()[0], inplace=True)
    else:  # if column is numeric
        df[column].fillna(df[column].median(), inplace=True)

# Dropping rows with missing values
df.dropna(inplace=True)

# Displaying cleaned data
print("\\nCleaned Data:")
print(df)