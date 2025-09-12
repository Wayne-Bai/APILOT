import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import learning_curve
from sklearn.svm import SVC

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Estimator
estimator = SVC(kernel='linear')

# Define parameters for learning curve
train_sizes, train_scores, test_scores = learning_curve(
    estimator, X, y, cv=5, scoring='accuracy', n_jobs=-1,
    train_sizes=np.linspace(0.1, 1.0, 10),
)

# Calculate mean and standard deviation of training score
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)

# Calculate mean and standard deviation of cross-validation score
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

# Plotting
plt.figure()
plt.plot(train_sizes, train_mean, color='r', marker='o', markersize=5, label='Training score')
plt.fill_between(train_sizes, train_mean + train_std, train_mean - train_std, color='r', alpha=0.05, lw=0)
plt.plot(train_sizes, test_mean, color='b', linestyle='--', marker='s', markersize=5, label='Cross-validation score')
plt.fill_between(train_sizes, test_mean + test_std, test_mean - test_std, color='b', alpha=0.05, lw=0)

# Details
plt.title('Learning Curve')
plt.xlabel('Training Examples')
plt.ylabel('Score')
plt.legend(loc='lower right')
plt.grid()
plt.show()
