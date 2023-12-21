# Use Python code to implement chi-square test
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2

# Load iris data
iris_dataset = load_iris()

# Create features and target
X = iris_dataset.data
y = iris_dataset.target

# Two features with the highest chi-squared statistics are selected
chi2_features = SelectKBest(chi2, k=2)
X_kbest_features = chi2_features.fit_transform(X, y)

# Reduced features
print('Original feature number:', X.shape[1])
print('Reduced feature number:', X_kbest_features.shape[1])
