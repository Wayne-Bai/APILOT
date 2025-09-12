from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

# Sample data creation with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 1, 1, 1],
    'C': [1, np.nan, 3, 4]
}

df = pd.DataFrame(data)

# Create an imputer object with a desired strategy
# Options: 'mean', 'median', 'most_frequent', or you can use a constant value
imputer_mean = SimpleImputer(strategy='mean')
imputer_median = SimpleImputer(strategy='median')
imputer_most_frequent = SimpleImputer(strategy='most_frequent')
imputer_constant = SimpleImputer(strategy='constant', fill_value=0)

# Impute missing values
df['A'] = imputer_mean.fit_transform(df[['A']])
df['B'] = imputer_most_frequent.fit_transform(df[['B']])
df['C'] = imputer_median.fit_transform(df[['C']])

# Optional: Impute with constant value
# df[['A', 'B', 'C']] = imputer_constant.fit_transform(df[['A', 'B', 'C']])

# Display the completed DataFrame
print(df)
