import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer

# Load your data into a pandas DataFrame
df = pd.read_csv('your_data.csv')

# Apply transformations to columns using the appropriate scaler
scalers = [StandardScaler(), MinMaxScaler(feature_range=(0, 1)), Normalizer()]
for scaler in scalers:
    df[column] = scaler.fit_transform(df[column])
