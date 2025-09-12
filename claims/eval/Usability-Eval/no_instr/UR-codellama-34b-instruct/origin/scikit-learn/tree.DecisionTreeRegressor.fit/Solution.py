from sklearn.tree import DecisionTreeRegressor
import pandas as pd

# Load your training data into a Pandas dataframe
df = pd.read_csv("your_data.csv")

# Split your data into features (X) and target (y)
X = df[["feature1", "feature2", ...]]  # Enter the column names of your features here
y = df["target"]

# Train a decision tree regressor on your training data
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# Use the trained model to make predictions on new data
predictions = regressor.predict(new_data)
