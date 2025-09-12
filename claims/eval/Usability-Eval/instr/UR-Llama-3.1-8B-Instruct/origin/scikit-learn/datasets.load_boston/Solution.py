# Import necessary libraries from scikit-learn and pandas
from sklearn import datasets
import pandas as pd

# Load the Boston house-prices dataset
boston_dataset = datasets.load_boston()

# Create a pandas DataFrame from the dataset
df = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
df['PRICE'] = boston_dataset.target

# Print the first 5 rows of the DataFrame
print(df.head())

# Print the info of the DataFrame (e.g., data types, number of missing values)
print(df.info())

# Print the first 5 rows of the summary statistics (e.g., mean, std, count)
print(df.describe().head())
