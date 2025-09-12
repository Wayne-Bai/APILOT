from sklearn.impute import SimpleImputer
import pandas as pd

# Sample DataFrame with missing values
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [None, None, 3, 4, 5]
}
df = pd.DataFrame(data)

# Creating SimpleImputer instance using mean
mean_imputer = SimpleImputer(strategy='mean')
df_imputed_mean = pd.DataFrame(mean_imputer.fit_transform(df), columns=df.columns)

# Creating SimpleImputer instance using median
median_imputer = SimpleImputer(strategy='median')
df_imputed_median = pd.DataFrame(median_imputer.fit_transform(df), columns=df.columns)

# Creating SimpleImputer instance using most frequent (mode)
mode_imputer = SimpleImputer(strategy='most_frequent')
df_imputed_mode = pd.DataFrame(mode_imputer.fit_transform(df), columns=df.columns)

# Creating SimpleImputer instance using a constant value
constant_imputer = SimpleImputer(strategy='constant', fill_value=0)
df_imputed_constant = pd.DataFrame(constant_imputer.fit_transform(df), columns=df.columns)

print("Mean Imputed DataFrame:")
print(df_imputed_mean)

print("Median Imputed DataFrame:")
print(df_imputed_median)

print("Mode Imputed DataFrame:")
print(df_imputed_mode)

print("Constant Imputed DataFrame:")
print(df_imputed_constant)
