import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Generate synthetic binary classification data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a binary classifier
classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Get predictions and their probabilities
y_scores = classifier.predict_proba(X_test)[:, 1]

# Display Precision-Recall curve
PrecisionRecallDisplay.from_predictions(y_test, y_scores)
plt.title('Precision-Recall Curve')
plt.show()
