# Import necessary libraries from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
from sklearn_pandas import DataFrameMapper
import pandas as pd

# Load Boston housing dataset
boston = load_boston()

# Convert dataset to DataFrame
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['PRICE'] = boston.target

# Map categorical data to numerical values
mapper = DataFrameMapper([
    ('CHAS', None),
    ('NOX', None),
    ('RM', None),
    ('AGE', None),
    ('DIS', None),
    ('RAD', None),
    ('TAX', None),
    # ('PTRATIO', None),
    ('B', None),
    ('LSTAT', None),
], df_out=True)
df_mapped = mapper.fit_transform(df)
df_mapped.head()

# Split dataset into features and target
X = df_mapped.drop('PRICE', axis=1)
y = df_mapped['PRICE']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Gradient Boosting Regressor
gbreg = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, 
                                  min_samples_split=2, min_samples_leaf=2, loss='ls')

# Train the model
gbreg.fit(X_train, y_train)

# Make predictions
y_pred = gbreg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean squared error:", mse)
