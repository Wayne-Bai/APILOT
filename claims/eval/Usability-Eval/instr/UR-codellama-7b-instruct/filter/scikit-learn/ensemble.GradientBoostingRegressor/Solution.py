
from sklearn.ensemble import GradientBoostingRegressor
from sklint.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the data
df = ...

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['feature1', 'feature2']], df['target'], test_size=0.2, random_state=42)

# Initialize the GradientBoostingRegressor object
gb = GradientBoostingRegressor()

# Train the model using the training data
gb.fit(X_train, y_train)

# Make predictions on the test data
y_pred = gb.predict(X_test)

# Evaluate the performance of the model using mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
