import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Load your dataset
df = pd.read_csv('your_data.csv')

# Split your data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['feature1', 'feature2']], df['target'], test_size=0.2, random_state=42)

# Initialize the GradientBoostingRegressor class with the desired parameters
gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Train the model on the training data
gb.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = gb.predict(X_test)

# Print the mean squared error
print("Mean Squared Error:", np.mean((y_test - y_pred) ** 2))
