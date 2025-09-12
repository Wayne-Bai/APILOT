from sklearn.naive_bayes import BernoulliNB

# Example data: features and labels
# Assuming binary features (0 and 1) representing the presence or absence of a feature
X = [[0, 1, 0], [1, 0, 1], [0, 0, 1], [1, 1, 0]]
y = [0, 1, 0, 1]  # Corresponding labels for each feature set

# Create a Bernoulli Naive Bayes model
model = BernoulliNB()

# Train the model
model.fit(X, y)

# Predict using the same data
predictions = model.predict(X)

# Output the predictions
print("Predictions:", predictions)
