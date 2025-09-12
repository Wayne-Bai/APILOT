from sklearn.model_selection import train_test_split
from sklearn.metrics import sigmoid_curve
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# Generate a binary classification dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a simple binary classifier
model = LogisticRegression()
model.fit(X_train, y_train)

# Compute predicted probabilities
y_proba = model.predict_proba(X_test)[:, 1]

# Compute true and predicted probabilities for calibration
true_probabilities = sigmoid_curve_(y_test)
confidence_levels = [i / 10 for i in range(1, 11)]

# Display the true and predicted probabilities in a plot (optional)
y_true = [1 if i > 0.5 else 0 for i in y_test]
