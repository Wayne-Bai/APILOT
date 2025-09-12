import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import PrecisionRecallDisplay

# Generate a binary classification dataset
X, y = make_classification(n_samples=1000, n_features=20,
                           n_classes=2, random_state=42)

# Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Plotting Precision-Recall curve
display = PrecisionRecallDisplay.from_estimator(model, X_test, y_test)
display.ax_.set_title('Precision-Recall curve')
plt.show()
