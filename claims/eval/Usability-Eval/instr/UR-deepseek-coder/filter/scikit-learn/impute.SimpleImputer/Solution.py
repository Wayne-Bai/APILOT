import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# Sample data with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, np.nan]
}

df = pd.DataFrame(data)

# Imputation strategies: 'mean', 'median', 'most_frequent', 'constant'
imputer_mean = SimpleImputer(strategy='mean')
imputer_median = SimpleImputer(strategy='median')
imputer_most_frequent = SimpleImputer(strategy='most_frequent')
imputer_constant = SimpleImputer(strategy='constant', fill_value=-999)

# Apply imputation
df_imputed_mean = pd.DataFrame(imputer_mean.fit_transform(df), columns=df.columns)
df_imputed_median = pd.DataFrame(imputer_median.fit_transform(df), columns=df.columns)
df_imputed_most_frequent = pd.DataFrame(imputer_most_frequent.fit_transform(df), columns=df.columns)
df_imputed_constant = pd.DataFrame(imputer_constant.fit_transform(df), columns=df.columns)

# Display results
print("Original DataFrame:")
print(df)
print("\nDataFrame after mean imputation:")
print(df_imputed_mean)
print("\nDataFrame after median imputation:")
print(df_imputed_median)
print("\nDataFrame after most frequent imputation:")
print(df_imputed_most_frequent)
print("\nDataFrame after constant imputation:")
print(df_imputed_constant)
