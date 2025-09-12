# Importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
import numpy as np
import pandas as pd

# Creating a sample dataset
np.random.seed(0)
data = {
    'Feature1': np.random.rand(100),
    'Feature2': np.random.rand(100),
    'Target': np.random.rand(100)
}
df = pd.DataFrame(data)

# Defining features (X) and target (y)
X = df[['Feature1', 'Feature2']]
y = df['Target']

# Splitting the dataset into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating a decision tree regressor
regressor = DecisionTreeRegressor(random_state=42)

# Training the model
regressor.fit(X_train, y_train)

# Making predictions
y_pred = regressor.predict(X_test)

# Evaluating the model
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
