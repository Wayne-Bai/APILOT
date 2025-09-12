from sklearn.linear_model import LogisticRegression

# Create a Logistic Regression model
lr_model = LogisticRegression()

# Assuming we have features X and targets y in our dataset
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the model with the training data
lr_model.fit(x_train, y_train)

# Make predictions on the testing data
predictions = lr_model.predict(x_test)

# Evaluate the model
accuracy = lr_model.score(x_test, y_test)
print("Model Accuracy: ", accuracy)
