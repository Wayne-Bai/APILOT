
from sklearn.impute import SimpleImputer

# Define the strategy for imputation (mean, median, most_frequent, constant)
strategy = 'mean'

# Create the SimpleImputer object with the specified strategy
imputer = SimpleImputer(strategy=strategy)

# Fit the imputer on the data
imputer.fit(data)

# Transform the data by replacing missing values
data_imputed = imputer.transform(data)
