from sklearn.impute import SimpleImputer
import numpy as np

# Create a dataset with missing values
data = np.array([[1, 2, np.nan], [3, 4, 5], [6, np.nan, 8]])

# Create a SimpleImputer object
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# Fit and transform the data
imputed_data = imputer.fit_transform(data)

# Print the imputed data
print(imputed_data)
