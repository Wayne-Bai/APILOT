import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Generate a binary classification dataset.
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the dataset into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model.
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict probabilities for the test set.
y_prob = model.predict_proba(X_test)[:, 1]

# Compute precision and recall values.
precision, recall, _ = precision_recall_curve(y_test, y_prob)

# Plot the precision-recall curve.
plt.plot(recall, precision, label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()
