from sklearn.impute import SimpleImputer

# Assuming X is your data
imputer = SimpleImputer(strategy='mean')  # or 'median' or 'most_frequent' or 'constant'
X_imputed = imputer.fit_transform(X)
