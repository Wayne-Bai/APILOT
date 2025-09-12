from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

# Sample data with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, 2, 3, np.nan]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the SimpleImputer with desired strategy
# Options for strategy: 'mean', 'median', 'most_frequent', or use a 'constant' value
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on the DataFrame and transform to fill missing values
df_imputed = imputer.fit_transform(df)

# Convert the result back to a DataFrame
df_filled = pd.DataFrame(df_imputed, columns=df.columns)

print(df_filled)
