import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Example dataframe
data = pd.DataFrame({
    'Color': ['Red', 'Green', 'Blue', 'Red', 'Green', 'Blue'],
    'Size': ['Small', 'Medium', 'Large', 'Small', 'Medium', 'Large']
})

# Initialize the OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)

# Fit and transform the categorical data
encoded_data = encoder.fit_transform(data[['Color', 'Size']])

# Create a dataframe from the encoded data
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Color', 'Size']), index=data.index)

print(encoded_df)
