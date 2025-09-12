from sklearn.linear_model import LinearRegression

# Import some data to train the model
X = [[0, 1], [1, 2], [2, 3]]
y = [2, 4, 6]

# Create a linear regression object and fit the data
reg = LinearRegression().fit(X, y)

# Use the trained model to make predictions on new data
new_data = [[3, 4], [5, 7]]
predictions = reg.predict(new_data)

print(predictions)
