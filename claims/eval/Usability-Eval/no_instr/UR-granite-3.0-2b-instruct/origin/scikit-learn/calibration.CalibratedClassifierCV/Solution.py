from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Generate a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Make predictions on the test set
y_pred_lr = lr.predict(X_test)

# Train an isotonic regression model
ir = IsotonicRegression()
ir.fit(X_train, y_train)

# Make predictions on the test set using isotonic regression
y_pred_ir = ir.predict(X_test)

# Calculate the accuracy of the logistic regression model
accuracy_lr = accuracy_score(y_test, y_pred_lr)

# Calculate the accuracy of the isotonic regression model
accuracy_ir = accuracy_score(y_test, y_pred_ir)

# Print the accuracy of both models
print("Logistic Regression Accuracy:", accuracy_lr)
print("Isotonic Regression Accuracy:", accuracy_ir)
