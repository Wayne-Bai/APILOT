from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import numpy as np

# Assuming X is your dataset with missing values
X = np.array([[1, 2, np.nan],
              [4, np.nan, np.nan],
              [7, 8, 9]])

# Initialize the SimpleImputer with the strategy 'mean' (or 'median' or 'most_frequent')
imputer = SimpleImputer(strategy='mean')

# Fit and transform the imputer on the dataset
X_imputed = imputer.fit_transform(X)

# If you want to use the imputed values for further processing, you can access them like this:
# imputed_values = imputer.transform(X)

# If you want to use the scaler on the imputed values, you can do it like this:
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X_imputed)
