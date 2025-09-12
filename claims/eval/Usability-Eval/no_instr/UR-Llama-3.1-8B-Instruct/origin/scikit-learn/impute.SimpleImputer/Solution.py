# Import necessary libraries
from sklearn.impute import SimpleImputer
from sklearn.impute._base import DesiredStatisticalMoment
import numpy as np
from sklearn.metrics import accuracy_score
import pandas as pd

# Create a sample dataset with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [6, np.nan, 8, 9, 10],
    'C': [np.nan, 12, 13, 14, 15]
}
df = pd.DataFrame(data)

# Print the original dataset with missing values
print("Original Dataset:")
print(df)

# Define imputation strategies
strategies = {
   'mean': SimpleImputer(missing_values=np.nan, strategy='mean'),
   'median': SimpleImputer(missing_values=np.nan, strategy='median'),
   'most_frequent': SimpleImputer(missing_values=np.nan, strategy='most_frequent'),
    'constant': SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)
}

# Impute missing values using different strategies
for name, imputer in strategies.items():
    imputed_data = imputer.fit_transform(df)
    imputed_df = pd.DataFrame(imputed_data, columns=df.columns)
    
    # Print the imputed dataset
    print(F"Imputed Dataset using {name} strategy:")
    print(imputed_df)
    print("\n")
