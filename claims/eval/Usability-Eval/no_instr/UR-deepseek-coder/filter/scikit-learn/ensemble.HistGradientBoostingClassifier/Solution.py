import numpy as np
from sklearn.experimental import enable_hist_gradient_boosting  # noqa
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example dataset
X = np.random.rand(100, 10)  # 100 samples, 10 features
y = np.random.randint(2, size=100)  # Binary classification target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Histogram-based Gradient Boosting Classification Tree
hgbc = HistGradientBoostingClassifier(random_state=42)

# Train the model
hgbc.fit(X_train, y_train)

# Make predictions
y_pred = hgbc.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
