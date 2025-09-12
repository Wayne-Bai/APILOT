from sklearn.impute import SimpleImputer
import numpy as np

# create a sample dataset with missing values
data = [[1, 2, np.nan], [3, 4, 6], [np.nan, 6, 8]]

# create an instance of the SimpleImputer class
imputer = SimpleImputer(missing_values=np.nan)

# use the mean strategy to replace missing values with the mean along each column
imputed_data = imputer.fit_transform(data, strategy='mean')
print(imputed_data)
