import pandas as pd
from sklearn.datasets import fetch_openml

# Load the Boston house-prices dataset
boston = fetch_openml(name='boston', version=1)

# Convert to DataFrame
boston_df = pd.DataFrame(data=boston.data, columns=boston.feature_names)
boston_df['PRICE'] = boston.target

# Display the first few rows of the dataset
print(boston_df.head())
