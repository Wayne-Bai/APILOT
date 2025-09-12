import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

# Generate a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=5, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the base estimator (RandomForestClassifier in this case)
estimator = RandomForestClassifier(n_estimators=100, random_state=42)

# Initialize RFE with the base estimator and the desired number of features to select
rfe = RFE(estimator, n_features_to_select=10)

# Fit RFE to the training data
rfe.fit(X_train, y_train)

# Transform the training and testing data to include only the selected features
X_train_selected = rfe.transform(X_train)
X_test_selected = rfe.transform(X_test)

# Print the ranking of the features
print("Feature ranking:")
for i in range(X.shape[1]):
    print(f"Feature {i}: Rank {rfe.ranking_[i]}")
