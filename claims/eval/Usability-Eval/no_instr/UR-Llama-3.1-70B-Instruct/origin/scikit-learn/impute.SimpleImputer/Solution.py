# Importing necessary libraries
import numpy as np
from sklearn.impute import SimpleImputer
import pandas as pd

# Creating a dataset with missing values
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, 5]}
df = pd.DataFrame(data)

print("Original DataFrame with missing values:")
print(df)

# Univariate Imputer for completing missing values using mean strategy
imputer_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
df_imputed_mean = pd.DataFrame(imputer_mean.fit_transform(df), columns=df.columns)

print("\nDataFrame with missing values replaced by mean:")
print(df_imputed_mean)

# Univariate Imputer for completing missing values using median strategy
imputer_median = SimpleImputer(missing_values=np.nan, strategy='median')
df_imputed_median = pd.DataFrame(imputer_median.fit_transform(df), columns=df.columns)

print("\nDataFrame with missing values replaced by median:")
print(df_imputed_median)

# Univariate Imputer for completing missing values using most_frequent strategy
imputer_most_frequent = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
df_imputed_most_frequent = pd.DataFrame(imputer_most_frequent.fit_transform(df), columns=df.columns)

print("\nDataFrame with missing values replaced by most_frequent:")
print(df_imputed_most_frequent)

# Univariate Imputer for completing missing values using constant value
imputer_constant = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)
df_imputed_constant = pd.DataFrame(imputer_constant.fit_transform(df), columns=df.columns)

print("\nDataFrame with missing values replaced by constant (0):")
print(df_imputed_constant)
