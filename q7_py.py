import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

# Load the data
data = pd.read_csv(r'N:\Education\coding_code\python\iris.csv')

# Print column names
print("Column Names:", data.columns)

# Separate data points and labels
data_points = data.iloc[:, :4]  # Selecting the first four columns as data points
labels = data['species']  # Use 'species' as the target variable

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(data_points, labels, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
scaler.fit(x_train)
x_train_std = scaler.transform(x_train)
x_test_std = scaler.transform(x_test)

# a. Use Support vector machine (SVM) to build a model
svm = SVC(kernel='rbf', random_state=0, gamma=0.10, C=1.0)
svm.fit(x_train_std, y_train)
print('Support Vector Machine:')
print('Training data accuracy: {:.2f}'.format(svm.score(x_train_std, y_train) * 100))
print('Testing data accuracy: {:.2f}'.format(svm.score(x_test_std, y_test) * 100))


# b. Use K Nearest Neighbour (KNN) to build a model
knn = KNeighborsClassifier(n_neighbors=7, p=2, metric='minkowski')
knn.fit(x_train_std, y_train)
print('\nK Nearest Neighbour:')
print('Training data accuracy: {:.2f}'.format(knn.score(x_train_std, y_train) * 100))
print('Testing data accuracy: {:.2f}'.format(knn.score(x_test_std, y_test) * 100))

# c. Use Decision tree classifier to build a model
decision_tree = tree.DecisionTreeClassifier(criterion='gini')
decision_tree.fit(x_train_std, y_train)
print('\nDecision Tree Classifier:')
print('Training data accuracy: {:.2f}'.format(decision_tree.score(x_train_std, y_train) * 100))
print('Testing data accuracy: {:.2f}'.format(decision_tree.score(x_test_std, y_test) * 100))

# d. Use Random forest (RF) classifier to build a model
random_forest = RandomForestClassifier()
random_forest.fit(x_train_std, y_train)
print('\nRandom Forest Classifier:')
print('Training data accuracy: {:.2f}'.format(random_forest.score(x_train_std, y_train) * 100))
print('Testing data accuracy: {:.2f}'.format(random_forest.score(x_test_std, y_test) * 100))