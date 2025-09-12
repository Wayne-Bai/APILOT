
from sklearn.impute import SimpleImputer

# Create a simple imputation strategy for replacing missing values
imputer = SimpleImputer(strategy='mean')

# Fit the imputation strategy to the data
imputer.fit(X)

# Replace missing values in the data with the imputed values
X_imp = imputer.transform(X)
