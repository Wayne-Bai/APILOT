import numpy as np
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier

# Sample data
X = np.array([[0, 0, 1], [1, 1, 0], [2, 2, 1], [3, 3, 0]])
y = np.array([0, 1, 1, 0])

# Create a random forest classifier
forest = RandomForestClassifier(n_estimators=100, random_state=42)

# Use SelectFromModel for feature selection based on importance weights
selector = SelectFromModel(forest)
selector.fit(X, y)

# Transform data to select important features
X_selected = selector.transform(X)
print("Shape of X after feature selection: ", X_selected.shape)
print("Selected features: ", X_selected)
