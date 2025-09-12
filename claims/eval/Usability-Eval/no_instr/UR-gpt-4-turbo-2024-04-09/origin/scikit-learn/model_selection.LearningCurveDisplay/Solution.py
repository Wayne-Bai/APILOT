import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.datasets import load_iris

# Load the data
data = load_iris()
X, y = data.data, data.target

# Create a pipeline with preprocessing and a classifier
pipeline = make_pipeline(StandardScaler(), SVC(kernel='linear'))

# Configure the learning curve
train_sizes, train_scores, test_scores = learning_curve(
    estimator=pipeline,
    X=X,
    y=y,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=10,
    scoring='accuracy',
    n_jobs=-1
)

# Calculate mean and standard deviation for training set scores
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)

# Calculate mean and standard deviation for test set scores
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

# Plot the learning curve
plt.fill_between(train_sizes, train_mean - train_std,
                 train_mean + train_std, color="blue", alpha=0.15)
plt.plot(train_sizes, train_mean, 'o-', color="blue", label="Training score")

plt.fill_between(train_sizes, test_mean - test_std,
                 test_mean + test_std, color="green", alpha=0.15)
plt.plot(train_sizes, test_mean, 'o-', color="green", label="Cross-validation score")

plt.title("Learning Curve")
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.legend(loc="best")
plt.show()
