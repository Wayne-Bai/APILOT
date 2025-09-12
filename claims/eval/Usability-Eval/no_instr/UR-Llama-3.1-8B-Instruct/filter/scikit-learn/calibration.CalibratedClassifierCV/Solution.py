# Importing the required libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import accuracy_score, brier_score_loss
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import numpy as np
import matplotlib.pyplot as plt

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and fit isotonic regression model
ir_model = IsotonicRegression()
ir_model.fit(X_train_scaled, y_train)

# Create and fit logistic regression model
lr_model = LogisticRegression()
lr_model.fit(X_train_scaled, y_train)

# Predict on test set
ir_pred = ir_model.predict_proba(X_test_scaled)[:, 1]
lr_pred = lr_model.predict_proba(X_test_scaled)[:, 1]

# Evaluate the models
print("Isotonic Regression Brier Score:", brier_score_loss(y_test, ir_pred))
print("Logistic Regression Brier Score:", brier_score_loss(y_test, lr_pred))

# Plot the non-parametric prediction probabilities using isotonic regression
plt.figure(figsize=(6, 6))
plt.plot(ir_pred)
plt.xlabel('sample index')
plt.ylabel('probability')
plt.title('Probabilities using Isotonic Regression')
plt.show()

# Plot the parametric prediction probabilities using logistic regression
plt.figure(figsize=(6, 6))
plt.plot(lr_pred)
plt.xlabel('sample index')
plt.ylabel('probability')
plt.title('Probabilities using Logistic Regression')
plt.show()
