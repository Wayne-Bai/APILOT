from sklearn.metrics import explained_variance_score

# Load your dataset
X, y = load_your_dataset()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a regression model on the training set
regressor = RandomForestRegressor()
regressor.fit(X_train, y_train)

# Predict the values for the testing set
y_pred = regressor.predict(X_test)

# Calculate the explained variance regression score
score = explained_variance_score(y_test, y_pred)
print("Explained Variance Score:", score)
