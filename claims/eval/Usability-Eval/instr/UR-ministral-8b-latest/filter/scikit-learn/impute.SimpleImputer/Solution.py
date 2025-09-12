import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import SimpleImputer

# Create a sample DataFrame
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, np.nan],
    'C': [1, np.nan, np.nan, 4]
}
df = pd.DataFrame(data)

# Initialize the imputer
imputer = SimpleImputer(strategy='mean')

# Fit and transform the data
imputed_data = imputer.fit_transform(df)

# Convert the array back to a DataFrame
imputed_df = pd.DataFrame(imputed_data, columns=df.columns)

print(imputed_df)
