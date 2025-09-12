import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_csv('data.csv')

# Initialize the scaler with the mean and standard deviation calculated during the transformation
scaler = StandardScaler(mean=df['mean'], std=df['std'])

# Apply the inverse transform on the scaled data
inv_scaled_data = scaler.inverse_transform(df)
