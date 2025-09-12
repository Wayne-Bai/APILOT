import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE

# Load the dataset
data = load_iris()
X = data.data
y = data.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the classifier
clf = RandomForestClassifier()

# Initialize RFE with the classifier
rfe = RFE(estimator=clf, n_features_to_select=2, step=1)

# Fit the RFE on the training data
rfe.fit(X_train, y_train)

# Get the ranked feature order
ranked_features = rfe.ranked_features_

print("Ranked Features:")
print(ranked_features)
