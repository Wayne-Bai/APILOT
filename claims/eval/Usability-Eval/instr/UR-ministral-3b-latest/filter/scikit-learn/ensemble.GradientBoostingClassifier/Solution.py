from sklearn.ensemble import GradientBoostingClassifier

# Initialize the classifier
gb = GradientBoostingClassifier(random_state=42)

# Fit the model to data
gb.fit(X_train, y_train)

# Make predictions on data
y_pred = gb.predict(X_test)
