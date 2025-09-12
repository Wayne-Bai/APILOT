import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import plot_partial_dependence
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# Generate a binary classification dataset.
X, y = make_classification(n_samples=1000, n_features=10, n_informative=2, n_redundant=0, random_state=42)

# Train a logistic regression model.
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Plot the partial dependence of the first two features.
plot_partial_dependence(model, [0, 1], response_method='predict_proba', n_jobs=1)
plt.show()
