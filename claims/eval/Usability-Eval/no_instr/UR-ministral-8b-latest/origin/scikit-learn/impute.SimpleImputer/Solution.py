from sklearn.impute import SimpleImputer

# Example DataFrame with missing values
import pandas as pd
data = {
    'A': [1, 2, None, 4, 5],
    'B': [10, None, 30, 40, 50],
    'C': [None, 'V', 'V', None, 'V']
}
df = pd.DataFrame(data)

# Create an instance of SimpleImputer
imputer = SimpleImputer(strategy='mean')

# Fit and transform the data to impute missing values
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print(df_imputed)
