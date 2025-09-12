from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Assuming you have a DataFrame df with a categorical column 'categorical_column'
# You can use the following code to one-hot encode the column

# Convert the DataFrame to a NumPy array
X = df['categorical_column'].values

# Initialize the OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Fit and transform the encoder on the data
X_encoded = encoder.fit_transform(X.reshape(-1, 1))

# If you want to apply the same transformation to new data, you can use the following code:
new_data = np.array(['new_value1', 'new_value2']).reshape(-1, 1)
X_new_encoded = encoder.transform(new_data)
