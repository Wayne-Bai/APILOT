
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Generate a random dataset for demonstration purpose
X = np.random.rand(100, 5)
y = np.random.randint(0, 2, size=100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a logistic regression model on the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Calculate precision and recall for different thresholds using the trained model
precision, recall, thresholds = precision_recall_curve(y_test, model.predict_proba(X_test))

# Plot the precision-recall curve
plt.plot(thresholds, precision[:-1], 'b', label='Precision')
plt.plot(thresholds, recall[:-1], 'r', label='Recall')
plt.legend()
plt.show()
