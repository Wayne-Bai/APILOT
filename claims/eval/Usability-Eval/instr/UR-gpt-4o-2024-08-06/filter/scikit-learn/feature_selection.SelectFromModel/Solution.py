import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.feature_selection import SelectFromModel

# Create a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2,
                           n_redundant=2, random_state=42, shuffle=False)

# Create a random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
clf.fit(X, y)

# Use SelectFromModel to select features based on importance weights
sfm = SelectFromModel(estimator=clf, threshold='mean', prefit=True)
X_selected = sfm.transform(X)

# Display the shape of the dataset before and after feature selection
print("Original number of features:", X.shape[1])
print("Reduced number of features:", X_selected.shape[1])
