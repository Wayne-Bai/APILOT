
import numpy as np
from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Generate some sample data
X = np.random.rand(100, 5)
y = np.random.randint(0, 2, size=100)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model on the training data
model = LogisticRegression().fit(X_train, y_train)

# Compute precision and recall for the test set
precision, recall, _ = precision_recall_curve(y_test, model.predict(X_test))

# Plot the precision-recall curve
plt.plot(recall, precision, label="Precision-Recall Curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.legend()
plt.show()
