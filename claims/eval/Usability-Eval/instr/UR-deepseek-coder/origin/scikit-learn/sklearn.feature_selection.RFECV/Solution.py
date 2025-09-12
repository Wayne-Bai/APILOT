import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier

# Generate a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=25, n_informative=3, n_redundant=2, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the RandomForestClassifier
estimator = RandomForestClassifier(n_estimators=100, random_state=42)

# Initialize RFECV with StratifiedKFold for cross-validation
rfecv = RFECV(estimator, step=1, cv=StratifiedKFold(5), scoring='accuracy')

# Fit the RFECV model to the training data
rfecv.fit(X_train, y_train)

# Transform the training and testing data to include only the selected features
X_train_selected = rfecv.transform(X_train)
X_test_selected = rfecv.transform(X_test)

# Print the number of selected features
print(f"Optimal number of features: {rfecv.n_features_}")

# Print the selected features
print(f"Selected features: {np.where(rfecv.support_)[0]}")
