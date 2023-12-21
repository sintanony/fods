from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Using Python code to implement PCA
iris = datasets.load_iris()
# rest of your code
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='FlowerType')

# Scatter plot of sepal length vs sepal width
plt.scatter(X['sepal length (cm)'], X['sepal width (cm)'], s=35, c=y, cmap=plt.cm.brg)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Sepal length vs. Sepal width')
plt.show()

# PCA
pca_iris = PCA(n_components=3).fit_transform(iris.data)

# 3D Scatter plot for the first three principal components
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(pca_iris[:, 0], pca_iris[:, 1], pca_iris[:, 2], cmap=plt.cm.Paired, c=iris.target)

for k in range(3):
    ax.scatter(pca_iris[y == k, 0], pca_iris[y == k, 1], pca_iris[y == k, 2], label=iris.target_names[k])

ax.set_title("First three P.C.")
ax.set_xlabel("P.C. 1")
ax.set_ylabel("P.C. 2")
ax.set_zlabel("P.C. 3")
plt.legend(numpoints=1)
plt.show()