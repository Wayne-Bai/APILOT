from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Suppose X and y are your data and target variables.
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree regressor.
model = DecisionTreeRegressor(random_state=42)

# Train the model using the training sets.
model.fit(X_train, y_train)

# To predict a new response with new data.
# predictions = model.predict(X_test)
