from sklearn.ensemble import GradientBoostingClassifier

# Define your features and target
X = ...
y = ...

# Create the model
model = GradientBoostingClassifier()

# Train the model
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
