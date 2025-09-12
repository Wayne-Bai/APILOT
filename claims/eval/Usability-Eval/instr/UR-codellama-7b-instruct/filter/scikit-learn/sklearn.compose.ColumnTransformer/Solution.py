
from sklearn import preprocessing
import pandas as pd

# Create a sample dataframe
data = {'A': [0, 1, 2, 3, 4], 'B': [5, 6, 7, 8, 9]}
df = pd.DataFrame(data)

# Define the columns to be transformed using scale transformer
columns_to_transform = ['A', 'B']

# Create a scale transformer object and fit the data
scale_transformer = preprocessing.MinMaxScaler()
scale_transformer.fit(df[columns_to_transform])

# Transform the data using the trained model
transformed_data = scale_transformer.transform(df[columns_to_transform])

# Print the transformed data
print(transformed_data)
