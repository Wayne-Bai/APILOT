import numpy as np
import pandas as pd
from sklearn.datasets import load_boston

# Load the Boston house-prices dataset
boston = load_boston()

# Convert the dataset to a pandas DataFrame for easier manipulation
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df['PRICE'] = boston.target

# Display the first few rows of the dataset
print(boston_df.head())
