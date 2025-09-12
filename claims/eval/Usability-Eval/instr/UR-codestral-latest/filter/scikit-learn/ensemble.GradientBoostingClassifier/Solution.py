from sklearn.ensemble import GradientBoostingClassifier

# Assume we have a dataset of features (X) and a target variable (y)
# For now, let's assume they are already defined

# Create and fit the model
model = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1)
model.fit(X, y)

# After training, the model can be used to predict the classes of new, unseen data
# Assume new_data is a list of features for prediction
predictions = model.predict(new_data)
