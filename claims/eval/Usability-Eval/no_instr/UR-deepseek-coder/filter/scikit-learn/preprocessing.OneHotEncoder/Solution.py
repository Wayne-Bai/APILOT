import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data
data = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'blue', 'red']
})

# Initialize the OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Fit and transform the data
encoded_data = encoder.fit_transform(data[['color']])

# Convert the encoded data to a DataFrame for better readability
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['color']))

print(encoded_df)
