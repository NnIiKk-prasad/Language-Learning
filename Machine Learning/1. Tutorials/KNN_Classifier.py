# *******K Nearest Neighbor Classification In Python*******
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading Datasets
iris = datasets.load_iris()

# Printing description
# print(iris.DESCR)

# Loading features and labels
features = iris.data
labels = iris.target

# Training the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

preds = clf.predict([[9.1, 9.5, 6.4, 0.2]])
print("Iris-Setosa" if preds == [0] else "Iris-Versicolour" if preds == [1] else "Iris-Virginica")
