import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
from sklearn.datasets import load_iris

# Load some data
iris = load_iris()
X = iris.data
y = iris.target

# Learn to predict each class against the other
svm = SVC(gamma=0.1, kernel="rbf", random_state=0)

# Calculate learning curves
train_sizes, train_scores, test_scores = learning_curve(svm, X, y, cv=5, scoring="accuracy", n_jobs=-1)

# Create means and standard deviations of training set scores
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)

# Create means and standard deviations of test set scores
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

# Draw learning curve
plt.figure()
plt.title("Learning Curves (SVM)")
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1, color="r")
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.1, color="g")
plt.plot(train_sizes, train_mean, 'o-', color="r", label="Training score")
plt.plot(train_sizes, test_mean, 'o-', color="g", label="Cross-validation score")
plt.legend(loc="best")
plt.show()
