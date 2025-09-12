from sklearn.impute import SimpleImputer
import numpy as np

# Creating sample data with missing values
data = [[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]]

# Create the SimpleImputer object with a specified strategy
# Strategies can be 'mean', 'median', 'most_frequent', or 'constant'
imputer = SimpleImputer(strategy='mean')

# Fit the imputer to the data and transform the data
imputed_data = imputer.fit_transform(data)

print(imputed_data)
