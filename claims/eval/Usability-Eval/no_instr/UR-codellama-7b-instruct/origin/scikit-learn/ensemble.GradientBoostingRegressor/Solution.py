import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv("data.csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[["feature1", "feature2", "feature3"]], df["target"], test_size=0.2, random_state=42)

# Create a Gradient Boosting Regressor object and fit it to the training data
gb_reg = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gb_reg.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = gb_reg.predict(X_test)

# Evaluate the model using mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error: ", mse)
