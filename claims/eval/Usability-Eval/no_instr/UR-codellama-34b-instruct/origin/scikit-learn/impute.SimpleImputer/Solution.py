from sklearn.impute import SimpleImputer
import numpy as np

# Load your dataset
data = ...

# Initialize the imputer with the strategy you want to use (mean, median, or most_frequent)
imp = SimpleImputer(missing_values=np.nan, strategy='mean')

# Fit the imputer to the data
imp.fit(data)

# Transform the data using the fitted imputer
imputed_data = imp.transform(data)
