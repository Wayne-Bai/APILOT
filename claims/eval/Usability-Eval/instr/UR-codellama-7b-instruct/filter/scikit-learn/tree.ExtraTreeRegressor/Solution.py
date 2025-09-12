
from sklearn.tree import ExtremelyRandomizedTreesRegressor

# Create an instance of ExtremelyRandomizedTreesRegressor
reg = ExtremelyRandomizedTreesRegressor(n_estimators=100, max_depth=5, random_state=42)

# Fit the model to the training data
reg.fit(X_train, y_train)

# Predict on the test data
y_pred = reg.predict(X_test)
