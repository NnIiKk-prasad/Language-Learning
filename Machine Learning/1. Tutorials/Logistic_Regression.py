# *******Coding Logistic Regression In Python*******
"""Task: Train a logistic regression classsifier to predict wether a flower is iris-verginica or not."""
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np


# loading iris dataset
iris = datasets.load_iris()

# loading features and lables
X = iris.data
y = (iris['target'] == 2).astype(np.int32)

# train a logistic regression classifier
clf = LogisticRegression()
clf.fit(X, y)

# estimated beta values and number of iterations
print("Estimated regression coefficients:\n", clf.coef_)
print("No. of iterations:", clf.n_iter_)

# predicted labels
y_pred = clf.predict(X)

# number of correctly predicted labels
print("Correctly predicted labels:", np.sum(y == y_pred))

# solver used by logistic regression
print("Solver used:", clf.solver)

# using matplotlib to plot the visualization
X0 = np.linspace(4, 8, 1000).reshape([-1, 1])
X1 = np.linspace(2, 5, 1000).reshape([-1, 1])
X2 = np.linspace(1, 7, 1000).reshape([-1, 1])
X3 = np.linspace(0, 3, 1000).reshape([-1, 1])
X_new = np.squeeze(np.array([X0, X1, X2, X3])).T
y_prob = clf.predict_proba(X_new)

plt.plot(X_new[:, 0], y_prob[:, 1], "g-", label="virginica")
plt.legend()
plt.show()
