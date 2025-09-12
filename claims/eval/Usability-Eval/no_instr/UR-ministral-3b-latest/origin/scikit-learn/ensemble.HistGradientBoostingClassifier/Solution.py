from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Histogram-based Gradient Boosting Classifier
hist_GB = GradientBoostingClassifier()

# Train the classifier
hist_GB.fit(X_train, y_train)

# Make predictions
y_pred = hist_GB.predict(X_test)

# Evaluate the classifier
accuracy = np.mean(y_pred == y_test)
print(f"Accuracy: {accuracy}")

# Plotting feature importance
importances = hist_GB.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure()
plt.title("Feature importance")
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), iris.feature_names[indices], rotation=90)
plt.xlim([-1, X.shape[1]])
plt.show()
