from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

# Sample data with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, np.nan, np.nan, 4]
}
df = pd.DataFrame(data)

# Create a SimpleImputer for different strategies
mean_imputer = SimpleImputer(strategy='mean')
median_imputer = SimpleImputer(strategy='median')
most_frequent_imputer = SimpleImputer(strategy='most_frequent')
constant_imputer = SimpleImputer(strategy='constant', fill_value=0)

# Apply the imputers to the DataFrame (for example, on column 'A')
df['A'] = mean_imputer.fit_transform(df[['A']])
df['B'] = median_imputer.fit_transform(df[['B']])
df['C'] = most_frequent_imputer.fit_transform(df[['C']])

# If you want to fill missing values in all columns with a constant value
df = constant_imputer.fit_transform(df)

# Convert back to DataFrame
df = pd.DataFrame(df, columns=['A', 'B', 'C'])

print(df)
