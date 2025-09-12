# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor as DTR 
from sklearn.tree import ExtraTreeRegressor as ETR
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the dataset (replace with your dataset)
# Assuming you have two numpy arrays X and y

# Create a decision tree regressor model
tree_model = DTR()

# Alternatively, you can use ExtraTreeRegressor for better performance
tree_model = ETR()

# Alternatively, you can use RandomForestRegressor for better performance
tree_model = RFR()

# Train the model using the training sets
tree_model = tree_model.fit(X, y)

# Make predictions using the test set
y_pred = tree_model.predict(X)

# The mean squared error
print("Mean squared error: %.2f" % np.sqrt(mean_squared_error(y, y_pred)))
