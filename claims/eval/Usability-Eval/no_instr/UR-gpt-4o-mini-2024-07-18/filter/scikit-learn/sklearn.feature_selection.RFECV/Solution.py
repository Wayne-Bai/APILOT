from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Create a model
model = RandomForestClassifier(n_estimators=100)

# Recursive Feature Elimination
selector = RFE(estimator=model, n_features_to_select=2)
selector = selector.fit(X, y)

# Summary of selected features
selected_features = selector.support_
print("Selected features:", selected_features)

# Evaluate model using cross-validation
scores = cross_val_score(model, X[:, selected_features], y, cv=5)
print("Cross-Validation Scores:", scores)
print("Mean Cross-Validation Score:", scores.mean())
