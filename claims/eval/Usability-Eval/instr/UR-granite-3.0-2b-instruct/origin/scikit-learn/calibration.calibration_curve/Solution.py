from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import calibration_curve
import matplotlib.pyplot as plt

# Generate a binary classification dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Compute true and predicted probabilities
y_pred_prob = model.predict_proba(X_test)[:, 1]
y_true_prob = y_test

# Compute calibration plot
plt.plot([0, 1], [0, 1], 'k--')
for q in [0.1, 0.5, 0.9]:
    plt.plot([y_true_prob[y_pred_prob <= q], y_true_prob[y_pred_prob > q]], [y_true_prob[y_pred_prob <= q], y_true_prob[y_pred_prob > q]], 'k-')
plt.xlabel('True probabilities')
plt.ylabel('Predicted probabilities')
plt.show()
