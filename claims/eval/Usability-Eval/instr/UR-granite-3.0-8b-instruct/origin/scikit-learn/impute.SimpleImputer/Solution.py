from sklearn.impute import SimpleImputer

# Create a SimpleImputer object with the desired strategy
imputer = SimpleImputer(strategy='mean')  # You can replace 'mean' with 'median' or 'most_frequent'

# Fit and transform the imputer on your data
# Assuming 'data' is your DataFrame and 'column_name' is the column you want to impute
imputed_data = imputer.fit_transform(data[['column_name']])

# Replace the original column with the imputed values
data['column_name'] = imputed_data
