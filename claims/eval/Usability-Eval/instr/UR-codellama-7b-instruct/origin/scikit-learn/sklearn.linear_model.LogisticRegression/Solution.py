
import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample data
X = np.array([[0,0], [1,1], [2,2]])
y = np.array([0,1,0])

# Initialize Logistic Regression model
clf = LogisticRegression()

# Train the model on the sample data
clf.fit(X, y)

# Make predictions for a new dataset
new_data = np.array([[3,3]])
prediction = clf.predict(new_data)
