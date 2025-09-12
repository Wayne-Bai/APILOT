from sklearn.datasets import make_classification
from sklearn.model_selection import learning_curve
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np

# Create a classification dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Define the model
model = LogisticRegression(max_iter=10000)

# Compute the learning curve
train_sizes, train_scores, test_scores = learning_curve(model, X, y,
                                                        cv=5,
                                                        scoring='accuracy',
                                                        train_sizes=np.linspace(0.1, 1.0, 10))

# Compute mean and variance
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

# Plot
plt.figure()
plt.plot(train_sizes, train_scores_mean, 'o-', color='r',
         label="Training Score")
plt.plot(train_sizes, test_scores_mean, 'o-', color='g',
         label="Cross-validation Score")

plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.1,
                 color='r')

plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.1,
                 color='g')

plt.grid()
plt.title('Learning Curve')
plt.xlabel('Training Size')
plt.ylabel('Accuracy Score')
plt.legend(loc="best")
plt.show()
