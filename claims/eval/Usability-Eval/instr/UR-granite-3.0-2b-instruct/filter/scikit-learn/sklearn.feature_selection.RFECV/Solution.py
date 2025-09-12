from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Assuming X is your feature matrix and y is your target variable
# X = ...
# y = ...

# Initialize the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Initialize Recursive Feature Elimination with cross-validation
rfe = RFE(clf, n_features_to_select=5, step=1)

# Fit the model to the data
rfe = rfe.fit(X, y)

# Print the selected features
print("Selected features:", X.columns[rfe.support_])
