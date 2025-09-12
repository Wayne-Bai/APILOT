import numpy as np
from sklearn.impute import SimpleImputer

# Let's create some example data with missing values
data = np.array([[1, 2, np.nan],
                 [4, np.nan, 6],
                 [np.nan, 8, 9],
                 [np.nan, np.nan, np.nan]])

# Define different strategies for imputation
strategies = ['mean', 'median', 'most_frequent']

for strategy in strategies:
    print(f"--- Strategy: {strategy} ---")
    imputer = SimpleImputer(strategy=strategy)
    imputed_data = imputer.fit_transform(data)
    print(imputed_data)
