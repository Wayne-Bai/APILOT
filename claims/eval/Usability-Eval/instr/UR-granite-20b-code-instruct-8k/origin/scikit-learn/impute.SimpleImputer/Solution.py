from sklearn.impute import SimpleImputer
import numpy as np

# Create an array with missing values
data = np.array([[1, 2, np.nan],
 [3, 4, 5],
 [np.nan, 6, 7]])

# Create an instance of the SimpleImputer class and fit the data
imputer = SimpleImputer(strategy='mean')
imputer.fit(data)

# Use the SimpleImputer to transform the data
transformed_data = imputer.transform(data)

print(transformed_data)
